# !/usr/bin/env python
# -*- coding: utf-8 -*-
 
sayi = input("Bir sayý giriniz:") # Kullanýcýdan bir sayý girmesi isteniyor
 
if sayi > 0:    # Girilen sayý 0'dan büyük ise
    print ("Sayý pozitiftir.")
    if sayi % 2 == 0:   # Sayý 0'dan büyük ve çift olmasý durumu
        print ("Sayý çifttir.")
    else:    # Sayý 0'dan büyük ve tek olmasý durumu
        print ("Sayý tektir.")
elif sayi < 0:    # Girilen sayý 0'dan küçük ise
    print ("Sayý negatiftir.")
else:     # Sayýnýn 0 olma durumu (if ve elif durumlarýnýn dýþýnda kalan bütün durumlar)
    print ("Sayý sýfýrdýr.")