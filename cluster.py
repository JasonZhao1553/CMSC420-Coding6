from __future__ import annotations
import json
import math
from typing import List
import numpy as np

class Graph():
    def  __init__(self,
            nodecount : None):
        self.nodecount = nodecount
        # IMPORTANT!!!
        # Replace the next line so the Laplacian is a nodecount x nodecount array of zeros.
        # You will need to do this in order for the code to run!
        self.A = np.zeros((nodecount, nodecount))
        self.D = np.zeros((nodecount, nodecount))
        self.laplacian = np.zeros((nodecount, nodecount))

    # Add an edge to the Laplacian matrix.
    # An edge is a pair [x,y].
    def addedge(self,edge):
        # Your code goes here.
        x = edge[0]
        y = edge[1]
        
        if self.A[x][y] == 1:
            return
        
        else:
            self.A[x][y] = 1
            self.A[y][x] = 1

            self.D[x][x] += 1
            self.D[y][y] += 1

            self.laplacian = self.D - self.A
        # Nothing to return.

    # Don't change this - no need.
    def laplacianmatrix(self) -> np.array:
        return self.laplacian

    # Calculate the Fiedler vector and return it.
    # You can use the default one from np.linalg.eig
    # but make sure the first entry is positive.
    # If not, negate the whole thing.
    def fiedlervector(self) -> np.array:
        # Replace this next line with your code.
        eigenvalues, eigenvectors = np.linalg.eig(self.laplacian)
        sorted_indices = np.argsort(eigenvalues)
        sorted_eigenvalues = eigenvalues[sorted_indices]
        sorted_eigenvectors = eigenvectors[:, sorted_indices]

        fvalue = sorted_eigenvalues[1]
        fvec = sorted_eigenvectors[:, 1]

        if fvec[0] < 0:
            return fvec * -1
        
        return fvec

    # Cluster the nodes.
    # You should return a list of two lists.
    # The first list contains all the indices with nonnegative (positive and 0) Fiedler vector entry.
    # The second list contains all the indices with negative Fiedler vector entry.

    def clustersign(self):
        # Replace the next two lines with your code.
        pind = []
        nind = []
        fvec = self.fiedlervector()
        for node_index, val in enumerate(fvec):
            if val < 0:
                nind.append(node_index)
            else:
                pind.append(node_index)
        # Return
        return([pind,nind])