# -*- coding: utf-8 -*-

"""
Undergraduate SEpita
Binary Trees: " - Hierarchical Implementation"
Tutorial - 2019-02
"""

from algopy import bintree
from algopy import queue


             
''' 
Trees as vector (list here) : 
using the hierarchical numbering
T[i] is the value at node number i (T[0] unused...)
'''


    
#------------------------------------------------------------------------------
#                             Examples

from algopy.bintree  import BinTree

B = BinTree(22, 
            BinTree(5, 
                    BinTree(3, BinTree(1, None, None), BinTree(4, None, None)), 
                    BinTree(12, None, BinTree(17, None, None))), 
            BinTree(29, BinTree(23, None, None), None))

# the "hierarchical" representation of tree B:
L = [None, 22, 5, 29, 3, 12, 23, None, 1, 4, None, 17, None, None, None, None, None, None, None, None, None, None, None, None]

# another example:

T_hier = [None]*30
for i in range(1, 9):
    T_hier[i] = i
(T_hier[11], T_hier[14], T_hier[29]) = (11, 14, 29)

#------------------------------------------------------------------------------
#  5.3                 Classics written with hierarchical representation

def size_h(T, i = 1):
    if (i >= len(T)) or (T[i] == None):
        return 0
    else:
        return 1 + size_h(T, 2*i) + size_h(T, 2*i+1)
        
def depth_pref_h(T, i = 1):
    if (i < len(T)) and (T[i] != None):
        print(T[i], end=' ')
        depth_pref_h(T, 2*i)
        depth_pref_h(T, 2*i+1)

def breadth(T):
    if len(T) > 1 and T[1] != None:
        l = len(T)
        q = queue.Queue()
        q.enqueue(1)
        while not q.isempty():
            no = q.dequeue()
            print(T[no])
            if 2 * no < l and T[2 * no] != None:   # left child
                q.enqueue(2 * no)
            if 2 * no + 1 < l and T[2 * no + 1] != None:   # right child
                q.enqueue(2 * no + 1)

    
#------------------------------------------------------------------------------           
#                     object implementation <-> hierarchical (list)
     
# from BinTree to hierarchical representation

# version1: the size is given (size)

def __hierFromTree(B, T, i=1):
    if B == None:
        T[i] = None
    else:
        T[i] = B.key
        __hierFromTree(B.left, T, 2*i)
        __hierFromTree(B.right, T, 2*i+1)

def hierFromTree(B, size):
    T = [None] * (2 ** maxi)
    __hierFromTree(B, T)
    return T

# version2: the list grows when needed (thanks to GolluM)

def extendList(L, i):
    for _ in range(len(L), i+1):
        L.append(None)
        
def __tree2hier(B, L, i = 1):
    if B !=  None:
        extendList(L, i)
        L[i] = B.key
        __tree2hier(B.left, L, 2 * i)
        __tree2hier(B.right, L, 2 * i + 1)
    
def tree2hier(B):
    L = [None]
    __tree2hier(B, L)
    return L
    
# q2: list -> object
# from hierarchical representation to BinTree

def hier2tree(L, i = 1):
    if i >= len(L) or L[i] == None:
        return None
    else:
        B = bintree.BinTree(L[i], None, None)
        B.left = hier2tree(L, 2*i)
        B.right = hier2tree(L, 2*i+1)
        return B
    
#       return BinTree(T[i], treeFromHier2(T, 2*i), treeFromHier2(T, 2*i+1))
    
    

