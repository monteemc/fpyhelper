# fpyhelper
Functional programing auxiliary functions in Python

Collection of fuctions to help whith fuctional style in Python

Functions avaliable:
reduce_cond1(f, p, inter, init)
and
reduce_cond2(f, p, inter, init)

Both are altrnatives to Functools Reduce, with aditional predicate p to interrupt the iteration when true. reduce_cond1 is to be used when the application of the function f is more expensive than the generation of the next value of the interable (e.g.: an eager list). reduce_cond2 when the application of the function f is cheaper than the generation of the next value of the interable (e.g.: a complex iterator).

The two probably will be optmized and unified with Python 3.8's "Assignment expressions" (PEP 572).


Still loking others additions to this lib...