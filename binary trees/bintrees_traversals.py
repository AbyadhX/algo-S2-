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

# with level change marks (None)
def width(B):
    """
    Computes B width (largeur)
    """
    w_max = 0
    if B:
        q = queue.Queue()
        q.enqueue(B)
        q.enqueue(None)
        w = 0
        while not q.isempty():
            B = q.dequeue()
            if B == None:
                w_max = max(w, w_max)
                if not q.isempty():
                    q.enqueue(None)
                    w = 0
            else:
                w = w + 1
                if B.left:
                    q.enqueue(B.left)
                if B.right:
                    q.enqueue(B.right)
    return w

# another way to manage levels, with two queues.                    
def width2(B): 
    """
    computes the width of a bintree
    """
    w_max = 0
    if B != None:
        q = queue.Queue() #current
        q.enqueue(B)
        q_next = queue.Queue() #next level
        w = 0
        while not q.isempty():
            B = q.dequeue()
            w = w + 1
            if B.left != None:
                q_next.enqueue(B.left)
            if B.right != None:
                q_next.enqueue(B.right)
            if q.isempty():
                w_max = max(w, w_max)
                (q, q_next) = (q_next, q)
                w = 0
    return w_max
