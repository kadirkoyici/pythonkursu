# -*- coding: utf-8 -*-

liste = [[1,"z"],9,"a"]
demet = ([1,"z"],9,"a")
sozluk = {"key1":[1,"z"],"key2":9,"key3":"a"}

print "\n Listem eleman indisleri ve Degerleri : ", liste
for j,k in enumerate(liste):
    print j," : ",k
    
print "\n Demetim eleman indisleri ve Degerleri : ", demet
for j,k in enumerate(demet):
    print j," : ",k

print "\n Sozlukum eleman indisleri ve Degerleri : ", sozluk
for j,k in enumerate(sozluk):
    print j," : ",k," : ",sozluk[k]