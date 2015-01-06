#!/usr/bin/env python
#-*- coding:utf-8 -*-

#from ilkmodul import program
from    ilkmodul    import  faktoriyel, surum

print surum
#print program



print faktoriyel(5)

import ilkmodul
print ilkmodul.program

from ilkmodul import faktoriyel as fak
hesap = fak(10)
print hesap
print "\n ---- \n"

print "modul tipini sorgula : ",type(ilkmodul)
moduldegis= dir(ilkmodul)
print type(moduldegis)
print moduldegis
