# -*- coding: utf-8 -*-

a = [1,2,3,4,5]
b = iter(a)
print " b=iter(a) : ", b, "| type(b) : ", type(b)
while True:
    try:
        k = next(b)
    except StopIteration:
        break
    print k
print a.__iter__()


def foo():  
    print "ilk"  
    yield 1  
foo()