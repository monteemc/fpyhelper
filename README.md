# fpyhelper
Functional programing auxiliary functions in Python

Collection of fuctions to help whith fuctional style in Python

Functions avaliable:
reduce_cond1(f, p, inter, init)
and
reduce_cond2(f, p, inter, init)

Both are altrnatives to Functools Reduce, with aditional predicate p to interrupt the iteration when true. reduce_cond1 is to be used when the application of the function f is more expensive than the generation of the next value of the interable (e.g.: an eager list). reduce_cond2 when the application of the function f is cheaper than the generation of the next value of the interable (e.g.: a complex iterator).
The two probably will be optmized and unified with Python 3.8's "Assignment expressions" (PEP 572).

The idea to implement the function came from a post on Stack Overflow(1), from Grant Palmer(2). Have no idea who is he, but is a neat way to do solve the problem. 

Still loking others additions to this lib...



(1) https://stackoverflow.com/questions/3130352/stopping-a-reduce-operation-mid-way-functional-way-of-doing-partial-running-s/49887281#49887281

(2) https://stackoverflow.com/users/9447738/grant-palmer?tab=profile