#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Undergraduate Epita - S2#
Binary Trees: Traversals - DFS and BFS
Tutorial - 2019-10
"""


from algopy import bintree, queue

"""
DFS: Depth-First Search
"""


def dfs(B):
    if B == None:
        # terminal case
        pass
    else:
        # preorder
        dfs(B.left)
        #inorder
        dfs(B.right)
        #postorder
        
        
def myprint(x):
    print(x, sep='', end='')
  
  
def dfs_displayAA(B):
    """
    Display Algebraic Abstract Type representation of B
    """
    if B == None:
        myprint('_')
    else:
        myprint('<' + str(B.key) + ',')
        dfs_displayAA(B.left)
        myprint(',')
        dfs_displayAA(B.right)
        myprint('>')

"""
BFS: Breadth-First Search (Level order traversal)
"""

#simple: displays keys

def bfs(B): 
    if B != None:
        q = queue.Queue()
        q.enqueue(B)
        while not q.isempty():
            B = q.dequeue()
            print(B.key, end= ' ')
            if B.left != None:
                q.enqueue(B.left)
            if B.right != None:
                q.enqueue(B.right)


def width(B):
    """
    Computes B width (largeur)
    """
    #FIXME
    pass
    