# !/usr/bin/env python
# -*- coding: utf-8 -*-

print "Sayi yerine -> Harf string girilirse : except ValueError :  "
print "Sıfıra Bölünme -> except ZeroDivisionError:"
print "-------------------------------------------------------------"
try:
    print "İki Sayıyı Toplayan Program"
    Sayi1=int(raw_input("Birinci Sayı"))
    Sayi2=int(raw_input("İkinci Sayı"))
    print Sayi1+Sayi2
except ValueError:
    print "Sayı Girmelisiniz.!"
    
print "İki Sayının Bölümü"
print "-------------------------------------------------------------"
sayi1=int(raw_input("Birinci Sayı:"))
sayi2=int(raw_input("İkinci Sayı:"))
try:
    bolum=float(sayi1/sayi2)
  
    print bolum        
except ZeroDivisionError:
    print "Bir sayı 0'a bölünemez!"

print "İki Sayının Bölümü"
print "-------------------------------------------------------------"
sayi1=int(raw_input("Birinci Sayı:"))
sayi2=int(raw_input("İkinci Sayı:"))
try:
    bolum=float(sayi1/sayi2)
  
    print bolum        
except (ZeroDivisionError,ValueError):
    print "Bir Hata Oluştu!"
    