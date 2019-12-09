#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
November 2019
BST: S2#
"""

from algopy import bintree


###############################################################################

def nb_inter(B, a, b):
    """
    computes the number of values of the BST B in the interval [a, b[
    """
    if B == None:
        return 0
    elif B.key < a:
        return nb_inter(B.right, a, b)
    elif B.key > b:
        return nb_inter(B.left, a, b)
    else:
        return 1 + nb_inter(B.left, a, b) + nb_inter(B.right, a, b)


###############################################################################    
# test

def __testbst(B, inf, sup):
    if B == None:
        return True
    else:
        if B.key > inf and B.key <= sup:
            return __testbst(B.left, inf, B.key) \
                    and __testbst(B.right, B.key, sup)
        else:
            return False
        

def testbst(B):
    return __testbst(B, -float('inf'), float('inf'))


##################################################################
#
#           CLASSICS

# Researches

def minBST(B):
    """
    B != None
    """
    if B.left == None:
        return B.key
    else:
        return minBST(B.left)
    
def maxBST(B):
    """
    B != None
    """
    while B.right != None:
        B = B.right
    return B.key


def searchBST(B, x):
    if B == None or B.key == x:
        return B
    else:
        if x < B.key:
            return searchBST(B.left, x)
        else:
            return searchBST(B.right, x)

def searchBST_iter(B, x):
    while B != None and B.key != x:
        if x < B.key:
            B = B.left
        else:
            B = B.right
    return B

# insertions


def leaf_insert(B, x):
    if B == None:
        return bintree.BinTree(x, None, None)
    else:
        if x <= B.key:
            B.left = leaf_insert(B.left, x)
        else:
            B.right = leaf_insert(B.right, x)
        return B

def leaf_insert_iter(B, x):
    new = bintree.BinTree(x, None, None)
    P = None
    T = B
    while T != None:
        P = T
        if x <= T.key:
            T = T.left
        else:
            T = T.right
    
    if P == None:
        return new
    else:
        if x <= P.key:
            P.left = new
        else:
            P.right = new
        return B
    
"""
delete
"""



def del_bst(B, x):
    if B == None:
        return None
    else:
        if x == B.key:
            if B.left == None:
                return B.right
            elif B.right == None:
                return B.left
            else:
                B.key = maxBST(B.left)
                B.left = del_bst(B.left, B.key)
                return B
        else:
            if x < B.key:
                B.left = del_bst(B.left, x)
            else:
                B.right = del_bst(B.right, x)
            return B

# Optimization

def del_max_bst(B):
    """
    B != None
    """
    if B.right == None:
        return (B.left, B.key)
    else:
        (B.right, m) = del_max_bst(B.right)
        return (B, m)


def del_bst_opti(B, x):
    if B == None:
        return None
    else:
        if x == B.key:
            if B.left == None:
                return B.right
            elif B.right == None:
                return B.left
            else:
                (B.left, B.key) = del_max_bst(B.left)
                return B
        else:
            if x < B.key:
                B.left = del_bst_opti(B.left, x)
            else:
                B.right = del_bst_opti(B.right, x)
            return B


"""
root insertion
"""

def cut(B, x):
    if B == None:
        return (None, None)
    else:
        if B.key <= x:
            L = B
            (L.right , R) = cut(B.right, x)
        else:
            R = B
            (L, R.left) = cut(B.left, x)
        return (L, R)

def root_insertion(B, x):
    (L, R) = cut(B, x)
    return bintree.BinTree(x, L, R)
    
 

 
