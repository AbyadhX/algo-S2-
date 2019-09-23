# -*- coding: utf-8 -*-
"""
Sept. 2019
@author: nathalie
S2# tutorial: to see how to use stacks
"""

from algopy import stack

# a new stack
p = stack.Stack()
 
# all operation are implemented as method!
 
# stack.push (empiler)
p.push(1)
p.push(2)
p.push(3)

# stack.peek (sommet)
print(p.peek())

# stack.pop (sommet + dépiler)
print(p.pop())
print(p.peek())

# stack.isempty (est-vide)
print(p.isempty())
p.pop()
p.pop()
print(p.isempty())

