# -*- coding: utf-8 -*-
'''
bir generator'u yalnız bir kere for döngüsünde kullanabilirsiniz.
tüm elemanların hafızada tutulmaması. Generatorlar, sırası gelen elemanı üretip döndürür, 
daha sonra da bu elemanı unuturlar. Örneğin;
 for döngüsünde sıraları geldiklerinde oluşup, işleri bittikten sonra hafızadan siliniyorl
'''
mygenerator = (x*x*x for x in range(5))
print mygenerator, " ", type(mygenerator)
for k in mygenerator:
   print k
from math import sqrt
"""
Ekrana �unu basar:
0
1
8
27
64
"""
for k in mygenerator:
   print k
"""
Ekrana hi�bir �ey bas�lmaz, ��nk� mygenerator'u bir kere kulland�k ve bitti.
"""

a=[1,2,3,4,5]
mygen=(x for x in a )
print mygen, type(mygen)

for k in mygen:
    print k
    
a=[2,3,4,5]
mygen=(sqrt(x) for x in a )
print mygen, type(mygen)

for k in mygen:
    print k
    
    
print "\n demet icin yapalım"

a=(1,2,3,4)

mygener=(x**3 for x in a)
for k in mygener:
    print k

print "\n sozluk icin yapalım"
a={"key1":2,"key2":3,"key3":4}
print a
mygenerat=(x for x in a)
for k in mygenerat:
    print k, a[k]

print a[k]

listelower=["AbC","DeF","gHi"]
genupper=(x.upper() for x in listelower)

for k in genupper:
    print k,type(genupper)





