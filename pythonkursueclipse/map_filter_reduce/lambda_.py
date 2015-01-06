# -*- coding: utf-8 -*-
l1=["a","b","c"]
l2=[1,2,3]

f = lambda x, y : x + y
k = lambda x : x**x
print f(1,1),type(f(1,1))
print f(l1,l2),type(f(l1,l2))
print map(k,l2)

print "-"*40

g = lambda x: x**2
print g(8)

print "-"*40
''' önemli bir örnek '''
def make_incrementor (n): return lambda x: x + n
f = make_incrementor(2)
g = make_incrementor(6)
print f,g
print f(42), g(42)

print "-"*40

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print filter(lambda x: x % 3 == 0, foo)

print "-"*40

def coklu(z,y):
    return lambda i : i+z+y
a=coklu(1,2)
print a(3)











