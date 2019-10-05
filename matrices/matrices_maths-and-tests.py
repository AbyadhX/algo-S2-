# -*- coding: utf-8 -*-
"""
[S2] Matrices: maths and tests
September 2019
@author: Nathalie
"""

from algopy import matrix

#--------------------------------------------------------------------
# 1.3 - 1.4 mathematical operations
# matrices are not empty!
        
def matrixaddition(A, B):
    (l, c) = (len(A), len(A[0]))
    if (l,c) != (len(B), len(B[0])):
        raise Exception("Matrices have not same dimensions")
    M = matrix.init(l, c, 0)
    for i in range(l):
        for j in range(c):
            M[i][j] = A[i][j] + B[i][j]
    return M

def matrixproduct(A, B):
    m = len(A)
    n = len(A[0])
    if n != len(B):
        raise Exception("Incompatible dimensions")
    p = len(B[0])
    M = matrix.init(m, p, 0)
    for i in range(m):
        for j in range(p):
            for k in range(n):
                M[i][j] = M[i][j] + A[i][k] * B[k][j]
    return M

#--------------------------------------------------------------------
#Minimax

# returns the position of the minimum value of the maximums of each line 
# in the integer matrice M 

# 2 functions

def posMaxList(L):
    ''' maximum position of list L, not empty '''
    p = 0
    for i in range(1, len(L)):
        if L[i] > L[p]:
            p = i
    return p

def posMinimax(M):
    (min_i, min_j) = (0, posMaxList(M[0]))
    for i in range(1, len(M)):
        max_j = posMaxList(M[i])
        if M[i][max_j] < M[min_i][min_j]:
            (min_i, min_j) = (i, max_j)
    return (min_i, min_j)

# a single function
maxint = float('inf')

def posMinimax2(M):
    mini = maxint
    (min_i, min_j) = (0,0)
    (l, c) = (len(M), len(M[0]))
    for i in range(l):
        max_j = 0
        for j in range(1, c):
            if M[i][j] > M[i][max_j]:
                max_j = j
        if M[i][max_j] < mini:
            mini = M[i][max_j]
            (min_i, min_j) = (i, max_j)
    return (min_i, min_j)


#--------------------------------------------------------------------
# Gap maximum : maximum des écarts max des lignes d'une matrice non vide

def gapList(L):
    """
    L != []
    """
    valMin = L[0]
    valMax = L[0]
    for i in range(1, len(L)):
        valMin = min(valMin, L[i])
        valMax = max(valMax, L[i])
    return valMax - valMin

def maxGapMatrix(M):
    mgap = gapList(M[0])
    for i in range(1, len(M)):
        mgap = max(mgap, gapList(M[i]))
    return mgap


# in one function (gapList inlined)
def maxGapMatrix2(M):
    mgap = 0
    (l, c) = (len(M), len(M[0]))
    for i in range(l):
        valMin = M[i][0]
        valMax = M[i][0]
        for j in range(1, c):
            valMin = min(valMin, M[i][j])
            valMax = max(valMax, M[i][j])
        mgap = max(mgap, valMax - valMin)
    return mgap


#--------------------------------------------------------------------
# research
# matrix is not empty!

def searchMatrix(M, x):
    (i, lin, col) = (0, len(M), len(M[0]))
    found = -1
    while i < lin and found == -1:
        j = 0
        while j < col and M[i][j] != x:
            j += 1
        if j != col:
            found = j
        i += 1
    if found != -1:
        return (i-1, found)
    else:
        return (-1, -1)
        
#------------------------------------------------------------------------------
#                   symmetry


def symmetric(A):
    (l, c) = (len(A), len(A[0]))
    if l != c:
        raise Exception("not a square matrix")
    i = 0
    sym = True
    while i < l and sym:
        j = 0
        while j < i and A[i][j] == A[j][i]:
            j += 1
        sym = j == i
        i += 1
    return sym
