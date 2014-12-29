# -*- coding: utf-8 -*-
b=(["kavun", "karpuz", "cilek"],2,3,4,"beş")
print "demet in ilk elemani bir dizi ise : ",b[0]
print "bu dizi tipinde olan ilk elemanın elemanlarına erisim  : ", b[0][1]
b[0].append("muz")
print b

demet=("Lale","Gül","Papatya","Papatya","Gül")
print demet

print "Papatya kelimesinin 2. defa geçtiği indis",demet.index("Papatya",2)
print "Gül kelimeisinin 2. defa geçtiği indis  : ",demet.index("Gül",2) 

aranan = "Papatya"
print aranan ," kelimesinden : " , demet.count(aranan), " tane var."
demet=(["kavun", "karpuz", "çilek"],2,3,4,"beş")
a,b,c,d,e=demet
print a, type(a)
print b
print c, type(c)
print d
print e, type(e)