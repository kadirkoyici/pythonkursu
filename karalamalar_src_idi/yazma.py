#!/usr/bin/env python
# -*- coding: utf-8 -*-

sayi = int(raw_input("Bir say� girin. Ben size bu say�n�n "

"istedi�iniz kuvvetini hesaplayay�m: "))

kuvvet = int(raw_input("�imdi de %s say�s�n�n ka��nc� kuvvetini "

"hesaplamak istedi�inizi s�yleyin: " %sayi))

print "%s say�s�n�n %s. kuvveti %s olur." %(sayi, kuvvet, sayi ** kuvvet)