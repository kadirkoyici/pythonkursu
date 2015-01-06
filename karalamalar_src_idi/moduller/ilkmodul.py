#!/usr/bin/env python
#-*- coding:utf-8 -*-
 
program = "Python"
surum = "2.x"

def faktoriyel(sayi):
    global glb
    glb="Global değişkenler "
    fak = 1
    for i in range(sayi):
        fak= fak * (i+1)
    return fak

print glb