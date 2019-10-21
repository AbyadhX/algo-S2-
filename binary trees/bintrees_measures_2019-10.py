#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Undergraduate Epita - S2#
Binary Trees: measures
Tutorial - 2019-10
"""

from algopy import bintree

def size(B):
    """Computes B size
    Args:
        B (BinTree)
    Returns:
        int
    """
    if B == None:
        return 0
    else:
        return 1 + size(B.left) + size(B.right)

def height(B):
    """Computes B height
    Args:
        B (BinTree)
    Returns:
        int
    """
    if B == None:
        return -1
    else:
        return 1 + max(height(B.left), height(B.right))


def epl(B, depth=0):
    """Binary Tree External Path Length (longueur de cheminement externe)     
    
    Args:
        B (BinTree)
    Optional arg:
        depth (int): the actual depth from first root

    Returns:
        int
    """
    if B == None:
        return 0
    else:
        if B.left == None and B.right == None:  #leaf
            return depth
        else:
            return epl(B.left, depth+1) + epl(B.right, depth+1)
            
        
def __ead(B, depth=0):
    """Auxiliary function for binary tree external average depth.

    Args:
        B (BinTree)
        depth (int): the actual depth from first root

    Returns:
        (int, int): external path length, external node (leaf) count.
    """
    if B == None:
        return (0, 0)
    elif B.left == None and B.right == None:
        return (depth, 1)
    else:
        (sleft, nbleft) = __ead(B.left, depth+1) 
        (sright, nbright) = __ead(B.right, depth+1)
        return (sleft + sright, nbleft + nbright)

def ead(B):
    """Binary Tree External Average Depth (Profondeur moyenne externe)

    Args:
        B (BinTree).

    Returns:
        float: internal average depth if B not empty, else 0

    """
    if B == None:
        return 0
    else:
        (epl, leaves) = __ead(B)
        return epl / leaves

# A version (among others) without calls on empty children:

def __ead2(B, depth=0):
    """Auxiliary function for binary tree external average depth.

    Args:
        B (BinTree): not empty
        depth (int): the actual depth from first root

    Returns:
        (int, int): external path length, leaf count.
    """
    if B.left == None:
        if B.right == None:
            return (depth, 1)
        else:
            return __ead2(B.right, depth+1)
    else:
        (pleft, nbleft) = __ead2(B.left, depth+1) 
        if B.right == None:
            return (pleft, nbleft)
        else:
            (pright, nbright) = __ead2(B.right, depth+1)  
            return (pleft + pright, nbleft + nbright)

def ead2(B):
    """Binary Tree Internal Average Depth.

    Args:
        B (BinTree).

    Returns:
        float: external average depth if B not empty else 0

    """
    if B == None:
        return 0
    else:
        (epl, leaves) = __ead2(B)
        return epl / leaves      
