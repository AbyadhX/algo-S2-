#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Undergraduate Epita - S2#
Binary Trees: tests
Tutorial - 2019-10
"""

from algopy import bintree, queue


def equal(B1, B2):
   if B1 == None:
      return B2 == None
   elif B2 == None:
      return False
   elif B1.key == B2.key:
      return equal(B1.left, B2.left) and equal(B1.right, B2.right)
   else:
      return False

def equal2(B1, B2):
  if B1 == None or B2 == None:
      return B1 == None and B2 == None
  else:
      return (B1.key == B2.key) \
             and equal2(B1.left, B2.left) \
             and equal2(B1.right, B2.right)



#-------------------------------------------------------------
# test: degenerate?

# not the most optimized (to many tests)
def degenerate0(T):
    if T == None :
        return True
    elif T.left != None  and T.right != None :
        return False 
    else :
        return degenerate0(T.left) and degenerate0(T.right)
        
# the optimized version (only 2 tests each time)        
def __degenerate(B):
    '''
    B not empty
    '''
    if B.left == None:
        if B.right == None:
            return True
        else:
            return __degenerate(B.right)
    else:
        if B.right == None:
            return __degenerate(B.left)
        else:
            return False
            
def degenerate(B):
    return B == None or __degenerate(B)

# a nice version
def __degenerate2(B):
    '''
    B not empty
    '''
    leftEmpty = (B.left == None)
    if B.right == None:
        return leftEmpty or __degenerate2(B.left)
    else:
        return leftEmpty and __degenerate2(B.right)
        
def degenerate2(B):
    return B == None or __degenerate2(B)


