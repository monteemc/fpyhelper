"""
fpyhelper.py - Functional programing auxiliary functions in Python
"""
# Written by MonteEMC <mtegit@fastmail.com>
#   Copyright (C) 2019 MonteEMC

from functools import reduce

def reduce_cond1(f, p, inter, init):
    """
    Functools Reduce, with aditional predicate to interrupt the iteration when 
    true.
    To be used when the application of the function f is more expensive than the 
    generation of the next value of the interable (e.g.: an eager list).
    reduce_cond1 and reduce_cond2 probably will be unified with Python 3.8's 
    "Assignment expressions".

    The initial value is not optional
    """
    # Avances in the next iteration, but do not calculates f(x,y), only p(x)

    def stop_iter(rv=None):
        raise StopIteration(rv)

    try:
        return reduce(
            lambda x, y: f(x,y) if not p(x) else stop_iter(x), 
            inter, init)
    except StopIteration as e:
        return e.args[0]

def reduce_cond2(f, p, inter, init):
    """
    Functools Reduce, with aditional predicate to interrupt the iteration when 
    true.
    To be used when the application of the function f is cheaper than the 
    generation of the next value of the interable (e.g.: a complex iterator).
    reduce_cond1 and reduce_cond2 probably will be unified with Python 3.8's 
    "Assignment expressions".

    The initial value is not optional
    """
    # f(x,y) is evaued 3(3!!!) times inside the lambda to avoid the next
    # iteration

    def stop_iter(rv=None):
        raise StopIteration(rv)

    try:
        return reduce(
            lambda x, y: f(x,y) if not p(f(x,y)) else stop_iter(f(x,y)), 
            inter, init)
    except StopIteration as e:
        return e.args[0]
