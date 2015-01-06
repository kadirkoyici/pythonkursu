# -*- coding: utf-8 -*-

def fibogenerator():
    a,b = 1,1
    print " a: ",a," b:",b
    while True:
        yield b  # yield b adında bir generator dondurdu 
        a,b = b, a + b
        print " a: ",a," b:",b


for k in fibogenerator():
    if k > 10:
        #print k   -> 10 dan büyük olunca son fibonacci sayisini verir
        break