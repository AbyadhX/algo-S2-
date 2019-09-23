# -*- coding: utf-8 -*-
"""
Sept. 2019
@author: nathalie
S2# tutorial: evaluation of expressions
"""

from algopy import stack

def is_op(c):
    return c in ('+', '-', '/', '*', '//', '%')

def eval(op, a, b):
    '''
        :param op: a string that represent an operator (see is_op function)
        :param a, b: two values (int or float)
        :rtype: int or float
    '''
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '//':
        return a // b
    elif op == '%':
        return a % b
    else:
        raise Exception ("Unknown operator")


def split(s, sep = ' '):
    '''
    Return a list of the words in S, using sep as the delimiter string.
    '''
    val = ""
    L = []
    for c in s:
        if c != sep:
            val += c
        else:
            L.append(val)
            val = ""
    L.append(val)
    return L

def split2(s, sep=' '):
    i = 0
    n = len(s)
    L = []
    while i < n:
        val = ""
        while i < n and s[i] != sep:
            val += s[i]
            i += 1
        L.append(val)
        i += 1
    return L

def eval_rpn(L):
    """
    algo:
        init pile
        pour chaque élément e de L:
            si e est une valeur:
               l'empiler
            sinon #opérateur
                évaluation:
                  récupérer les 2 opérandes = dépiler
                  empiler le résultat de l'opération
    """
    p = stack.Stack()
    for e in L:
        #FIXME
        pass


