# -*- coding: utf-8 -*-

print "\n"

def creategeneratorSquare(l):
    for x in l: #dedi�ine g�re l nin bir liste demet gibi iterable degidken oldugunu anlad�ik
     yield x * x    #  generator dondurur

generator = creategeneratorSquare([1,2,3,4,5]) # l degiskenine biz liste gonderdik fonksiyon bize generator donderdi
for k in generator:
   print k


print "Sirali arguman kullanimi : \n * operatoru listeyi eleamlarina ayimiyor, sadece gelen argumanlari tek tek ayiriyor :\n "

def demet(*bolumler):
    for sira,bolum in enumerate(bolumler):
        print "%s : %s"%(sira,bolum)
 
listemsi=1,2,3,"a","b"
print "demet(listemsi) : "
demet(listemsi)   # tek arguman olarak listenin kendisini gpnderdi
print "\ndemet(*listemsi) : "

demet(*listemsi)

print "\n"
demet("Bilgisayar","Elektrik-Elektronik","Makina","İnşaat") # argumanlari * operatoru tek tek ayirdi

print "\n -------------------"

def bolum(bolum1,bolum2,bolum3,bolum4): #argumanlar isimleri belli
    print bolum1,bolum2,bolum3,bolum4
 
bolumler = ["Bilgisayar ","Elektrik-Elektronik ","Makina ","İnşaat "]

bolum(*bolumler)

print "------------------ sirali arguman - son - -----------------\n"



def myfonk(*m):
    for x in m:
        print x*x

listem1=[4,1,2,3]
demetim1=(15,1,2,3)

genmi=myfonk(*listem1)
print "\n"
genmi2=myfonk(*demetim1)
print type(genmi), genmi,type(genmi2), genmi2
