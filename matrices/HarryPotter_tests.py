# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:11:16 2019

@author: Nathalie
"""

from algopy import matrix
import HarryPotter as HP

T = [[3, 1, 7, 4, 2],
     [2, 1, 3, 1, 1],
     [1, 2, 2, 1, 8],
     [2, 2, 1, 5, 3],
     [2, 1, 4, 4, 4],
     [5, 2, 7, 5, 1]]

#-----------------------------------------------------------------------
# some examples to test


T15 = matrix.load("files/HarryPotter15.txt") # 129
T20 = matrix.load("files/HarryPotter20.txt") # 1676
T50 = matrix.load("files/HarryPotter50.txt") # 4200

def test(T):
    return (HP.HarryPotterGreedy(T),
            HP.HarryPotter(T),
            HP.HarryPotterBrutForce(T))

'''    
Some results:
>>> test(T15)
HarryPotterGreedy function took 0.0 ms
HarryPotter function took 0.0 ms
HarryPotterBrutForce function took 32703.341007232666 ms
((128, [10, 10, 11, 11, 10, 10, 9, 8, 7, 7, 8, 8, 7, 8, 9]), 129, 129)

>>> test(T20)
HarryPotterGreedy function tooks 0.0 ms
buildMaxMat function tooks 0.0 ms
HarryPotterBrutForce function tooks 11073955.830097198 ms (> 3h)

>>> HP.HarryPotterGreedy(T50)
HarryPotterGreedy function tooks 0.0 ms
>>> HP.HarryPotter(HP50)
HarryPotter function tooks 15.59591293334961 ms
'''
     