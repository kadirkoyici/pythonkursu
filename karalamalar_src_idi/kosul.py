# !/usr/bin/env python
# -*- coding: utf-8 -*-
 
sayi = input("Bir say� giriniz:") # Kullan�c�dan bir say� girmesi isteniyor
 
if sayi > 0:    # Girilen say� 0'dan b�y�k ise
    print ("Say� pozitiftir.")
    if sayi % 2 == 0:   # Say� 0'dan b�y�k ve �ift olmas� durumu
        print ("Say� �ifttir.")
    else:    # Say� 0'dan b�y�k ve tek olmas� durumu
        print ("Say� tektir.")
elif sayi < 0:    # Girilen say� 0'dan k���k ise
    print ("Say� negatiftir.")
else:     # Say�n�n 0 olma durumu (if ve elif durumlar�n�n d���nda kalan b�t�n durumlar)
    print ("Say� s�f�rd�r.")