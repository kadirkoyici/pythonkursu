#!/usr/bin/env python
# -*- coding: utf-8 -*-

sayi = int(raw_input("Bir sayý girin. Ben size bu sayýnýn "

"istediðiniz kuvvetini hesaplayayým: "))

kuvvet = int(raw_input("Þimdi de %s sayýsýnýn kaçýncý kuvvetini "

"hesaplamak istediðinizi söyleyin: " %sayi))

print "%s sayýsýnýn %s. kuvveti %s olur." %(sayi, kuvvet, sayi ** kuvvet)