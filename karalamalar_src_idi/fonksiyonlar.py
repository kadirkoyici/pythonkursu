# -*- coding: utf-8 -*-
def fonksiyon(isim,not1,not2):
    ortalama = (not1+not2)/2
    print isim,"adındaki öğrencinin not ortalaması:",ortalama
     
     
fonksiyon("Mazlum",80,90)
fonksiyon(not1=80,isim="Mazlum",not2=90)
print "-------- Varsayilan Degerdeki Argumanlar ------------------"
sayilar = range(14)
print sayilar
sayilar = range(6,14)
print sayilar
sayilar = range(6,14,2)
print sayilar

print " ---- 2 argumanli fonks 2. arguman default  1 e esit tek arguman olarak cagirildi ---------"
def topla(sayi,kacar=1):
    toplam = 0
    i=0
    while(sayi>i):
        toplam += i
        i+=kacar
    print "Toplam:",toplam
 
topla(10) #topla(10,)
topla(10, 3)
print "-----  istenen Sayida Sirali Arguman Kullanimi ------"
def ogrenci(*bilgiler):
    bilgi=""
    for i in bilgiler:
        bilgi+=i
    print "Ögrencinin bilgileri:\n",bilgi
 
ogrenci("Mazlum ","Teknoloji Fakütesi ","Bilgisayar Mühendisliği ","1.Sınıf")

 
def ogrenci2(*bilgiler):
    print bilgiler
 
ogrenci2("Mazlum ","Teknoloji Fakutesi ","Bilgisayar Muhendisligi ","1.Sinif")

def demet(*bolumler):
    for sira,bolum in enumerate(bolumler):
        print "%s : %s"%(sira,bolum)
 
demet("Bilgisayar","Elektrik-Elektronik","Makina","İnşaat")

print "---- bolum bolumler ----------"
def bolum(bolum1,bolum2,bolum3,bolum4):
    print bolum1,bolum2,bolum3,bolum4
 
bolumler = ["Bilgisayar ","Elektrik-Elektronik ","Makina ","İnşaat "]
 
bolum(*bolumler)

print "--- Ortalama Notlar * operatoru -----"

def ortalama(*notlar):
    toplam=0
    for ders in notlar:
        toplam+=int(ders)
    print toplam/len(notlar)
     
notlar = []
sayi=0
print "Öğrenci Notlarını Giriniz:\n"
derssayisi=int(raw_input("Ders sayisini girin: "))
print "ders sayisi  :  %s" %derssayisi
print "notlar isimli bir liste oluşturuluyor liste uzunlugu belli degildir"
while derssayisi>sayi:
    notlar.append(raw_input("Not:"))
    sayi+=1
 
ortalama(*notlar)








