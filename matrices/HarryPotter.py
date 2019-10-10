# -*- coding: utf-8 -*-
"""
Philosophers Stone
Oct. 2019
@author: Nathalie
"""
   


from algopy import matrix
from algopy import timing

# uncomment the lines @timing.timing if you want to see the durations!

def posMax(L):
    pos = 0
    for i in range(1, len(L)):
        if L[i] > L[pos]:
            pos = i
    return pos

#----------------- Greedy Algorith (algorithme glouton) ----------------------

#@timing.timing
def HarryPotterGreedy(T):
    col = len(T[0])
    j = posMax(T[0])
    s = T[0][j]
    for i in range(1, len(T)):
        jmax = j
        if j > 0 and T[i][j-1] > T[i][jmax]:
            jmax = j - 1
        if j < col - 1 and T[i][j+1] > T[i][jmax]:
            jmax = j + 1
        s += T[i][jmax]
        j = jmax

    return s

def HarryPotterGreedy_path(T):
    col = len(T[0])
    j = posMax(T[0])
    s = T[0][j]
    path = [j]
    for i in range(1, len(T)):
        jmax = j
        if j > 0 and T[i][j-1] > T[i][jmax]:
            jmax = j - 1
        if j < col - 1 and T[i][j+1] > T[i][jmax]:
            jmax = j + 1
        path.append(jmax)
        s += T[i][jmax]
        j = jmax

    return (s, path)


#----------------- Dynamic Programming ----------------------


def buildMaxMat(T):
    l = len(T)
    c = len(T[0])
    M = matrix.init(l, c, 0)

    for j in range(c):
        M[0][j] = T[0][j]

    for i in range(1, l):
        #FIXME
        pass
    
    return M
    
#@timing.timing
def HarryPotter(T):
    M = buildMaxMat(T)
    n = len(M)  # line nb
    return M[n-1][posMax(M[n-1])]
    
# BONUs: build the path

#----------------------------------------------------------------------
# Brut force... warning: can be long when l, c >= 15, 15

# without the path
def brut(T, i, j):
    if i == len(T)-1:
        return T[i][j]
    else:
        maxi = brut(T, i+1, j)
        if j > 0:
            maxi = max(maxi, brut(T, i+1, j-1))
        if j < len(T[0]) - 1:
            maxi = max(maxi, brut(T, i+1, j+1))
        return (maxi + T[i][j])
    
#@timing.timing
def HarryPotterBrutForce(T):
    
    maxi = 0
    for j in range(len(T[0])):
        maxi = max(maxi, brut(T, 0, j))
    return maxi
    
# BONUs: build the path

