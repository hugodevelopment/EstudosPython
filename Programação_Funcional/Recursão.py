"""
Recursion is a very important concept in functional programming.
The fundamental part of recursion is self-reference -- functions calling themselves. 
It is used to solve problems that can be broken up into easier sub-problems of the same type.
"""

# Ex1 : Uma função regressiva
def countdown(x):
    print(x)
    if x==0:
        return 
    else:
        countdown(x-1) 

countdown(10)            