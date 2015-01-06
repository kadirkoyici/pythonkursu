#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
def fonksiyon(**bilgiler):
    ortalama = (bilgiler["not1"]+bilgiler["not2"])/2
    print bilgiler["isim"],"adindaki ogrencinin not ortalamasi : ",ortalama
    print bilgiler
     
fonksiyon(not1=80,isim="Mazlum",not2=90)

def fonksiyon2(**bilgiler2):
    ortalama = (bilgiler2["not1"]+bilgiler2["not2"])/2
    print bilgiler2["isim"],"adındaki öğrencinin not ortalaması",ortalama
     
sozluk = {"not1":80,"isim":"Mazlum","not2":90}
fonksiyon2(**sozluk)

def not_ortalamasi(**ortalamalar):
    for i,k in ortalamalar.items():
        print "'",i,"' isimli öğrencinin not ortalaması:",k
     
 
ortalama = {"Mazlum":2.4,"Okan":2.7,"Sunay":3.2,"Nilay":3.0,"Sultan":2.6,"Mücahit":3.3}
not_ortalamasi(**ortalama)