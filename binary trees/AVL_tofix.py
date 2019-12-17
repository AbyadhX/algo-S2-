#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AVL: insertion & deletion
S2
"""

from algopy import avl



#------------------------------------------------------------------------------    
# rotations: works only in "usefull" cases

def lr(A): # rotation gauche
    aux = A.right
    A.right = aux.left
    aux.left = A
    aux.bal += 1
    A.bal = -aux.bal
    return aux

def rr(A): # rotation droite
    aux = A.left
    A.left = aux.right
    aux.right = A
    aux.bal -= 1
    A.bal = -aux.bal
    return aux

def lrr(A): # rotation gauche-droite
# left rotation on left child
    aux = A.left.right
    A.left.right = aux.left
    aux.left = A.left
# right rotation
    A.left = aux.right
    aux.right = A
    A = aux

    if A.bal == -1:
        (A.left.bal, A.right.bal) = (1, 0)
    elif A.bal == 1:
        (A.left.bal, A.right.bal) = (0, -1)
    else:
        (A.left.bal, A.right.bal) = (0, 0)
    A.bal = 0
    
    return A

def rlr(A): # rotation droite-gauche
    aux = A.right.left
    A.right.left = aux.right
    aux.right = A.right
    
    A.right = aux.left
    aux.left = A
    
    (aux.left.bal, aux.right.bal) = (0, 0)
    if aux.bal == -1:
        aux.left.bal = 1
    elif aux.bal == 1:
        aux.right.bal = 1
    aux.bal = 0

    return aux

"""
insertion
"""

def __insertAVL(x, A):
    """ 
    returns (the new tree, the height change): (AVL, bool)
    """
    if A == None:
        return (avl.AVL(x, None, None, 0), True)
    elif x == A.key:
        return (A, False)
    else:
        if x < A.key:
            (A.left, dh) = __insertAVL(x, A.left)
            if not dh:
                return (A, False)
            else:
                #FIXME
                pass
            
        else:   # x > A.key
            (A.right, dh) = __insertAVL(A.right, x)
            if not dh:
                return (A, False)
            else:
                #FIXME
                pass

#       all * can be replaced by a single return:
#       return (A, A.bal != 0)
            
            
def insertAVL(x, A):
    (A, dh) = __insertAVL(x, A)
    return A
        

def buildAVLfromList(L, A = None):
    for e in L:
        A = insertAVL(e, A)
    return A

# you can test your function with
L_tuto = [17, 9, 29, 3, 13, 23, 40, 1, 8, 11, 42]
# you should obtain the tutorial AVL!


"""
deletion
"""

# non optimized

def maxBST(B):
    while B.right != None:
        B = B.right
    return B.key
    
def __deleteAVL(x, A):
    """ 
    returns (the new tree, the height change): (AVL, bool)
    """    
    if A == None:
        return (None, False)
        
    elif x == A.key:
        # FIXME
                
    if x <= A.key:      
        (A.left, dh) = __deleteAVL(x, A.left)
        # FIXME
           
    else:   # x > A.key
        (A.right, dh) = deleteAVL(x, A.right)
        
        # FIXME
        
def deleteAVL(x, A):
    (A, _) = __deleteAVL(x, A)
    return A



