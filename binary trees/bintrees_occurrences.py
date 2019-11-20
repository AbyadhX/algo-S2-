#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Undergraduate Epita - S2
Binary Trees: occurrences
Tutorial - 2019-11
"""

from algopy import bintree, queue

#-------------------------------------------------------------
# Occurrences: build the list

# tree in the subject

# s1 = "{ε, 0, 1, 00, 01, 10, 11, 000, 011, 110, 1101}"

# another tree

# s2 = "{ε,0,1,00,10,11,000,001,111,0010,0011}"

def occurrences(B):
    L = []
    if B != None:
        q = queue.Queue()
        q.enqueue((B, ""))
        while not q.isempty():
            (B, occ) = q.dequeue()
            L.append(occ) 
            if B.left != None:
                q.enqueue((B.left, occ + '0'))
            if B.right != None:
                q.enqueue((B.right, occ + '1'))
        L[0] = chr(949)    # 'ε'
                
    return L



#-------------------------------------------------------------
# prefix code

# question 3: the tree

from algopy.bintree import BinTree

B = BinTree(' ', 
            BinTree('a', None, None),
            BinTree(' ', 
                    BinTree(' ', 
                            BinTree('c', None, None), 
                            BinTree('b', None, None)
                            ), 
                    BinTree(' ', 
                            BinTree(' ', 
                                    BinTree('f', None, None),
                                    BinTree('e', None, None)),
                            BinTree('d', None, None)
                            )
                    )
            )

# question 4
def __searchOcc(B, c, occ=""):
    if B.left == B.right:
        if B.key == c:
            return occ
        else:
            return ""
        
    else:
        res = __searchOcc(B.left, c, occ+'0')
        if res == "":
            res = __searchOcc(B.right, c, occ+'1')
        return res

        
def searchOcc(B, c):
    if B == None:
        return ""
    else:
        return __searchOcc(B, c)


    
