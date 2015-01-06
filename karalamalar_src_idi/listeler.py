# -*- coding: utf-8 -*-
from operator import index

cumle = ['hayat','python','ile','guzel']
print cumle
print "Listenin 2. eleman�:", cumle[1]
print "----------------------------------"

liste3 = [1,2,3,4,5,6,7,8,9]
print "Liste elemman sayisi :  %s " %len(liste3) 
print "----------------------------------"

cumle = ['hayat','python','ile','guzel']
print cumle[1:3]
print "----------------------------------"

cumle = ['hayat','python','ile','guzel']
print cumle[:2]

print "----------------------------------"
cumle = ['hayat','python','ile','guzel']
print cumle[1:]
print "----------------------------------"

liste4 = ["okan","vurdu","www.okanvurdu.net",1,3,4,"python"]
print "Liste 4 : " %cumle[1::2]

print "----------------------------------"

takimlar = ['Galatasaray','Fenerbahce','Besiktas']
print takimlar
takimlar.append('Trabzonspor')
print takimlar

print takimlar.index("Besiktas")
takimlar[0]="Besiktas"
print takimlar
takimlar.remove("Besiktas")
print takimlar
takimlar.append("Besiktas")
print takimlar

