from ilkmodul import program
from ilkmodul import faktoriyel

print program
print faktoriyel(5)

import ilkmodul
print program

import ilkmodul as ilk
hesap = ilk.faktoriyel(5)
print hesap

from ilkmodul import faktoriyel as fak
hesap = fak(5)
print hesap

print "sdfds", dir(ilkmodul).count(100)