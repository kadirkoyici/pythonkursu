# -*- coding: utf-8 -*-
def ogrenci(*bilgiler):
    bilgi=""
    for i in bilgiler:
        bilgi+=i
    print "Öğrencinin bilgileri : \n",bilgi
 
ogrenci("Mazlum ","Teknoloji Fakütesi ","Bilgisayar Mühendisliği ","1. Sınıf")

##-------------------------------------------------------------------------------------

def demet(*bolumler):
    for sira,bolum in enumerate(bolumler):
        print "%s : %s"%(sira,bolum)
 
demet("Bilgisayar","Elektrik-Elektronik","Makina","İnşaat")

##-------------------------------------------------------------------------------------

def bolum(bolum1,bolum2,bolum3,bolum4):
    print bolum1,bolum2,bolum3,bolum4
 
bolumler = ["Bilgisayar ","Elektrik-Elektronik ","Makina ","İnşaat "]
 
bolum(*bolumler)

##-------------------------------------------------------------------------------------

def ortalama(*notlar):
    toplam=0
    for ders in notlar:
        toplam+=int(ders)
    print toplam/len(notlar)
     
notlar = []
sayi=0
print "Öğrenci Notlarını Giriniz:\n"
while 5>sayi:
    notlar.append(raw_input("Not:"))
    sayi+=1
 
ortalama(*notlar)