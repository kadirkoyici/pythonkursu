#!/usr/bin/env python
# -*- coding: utf-8 -*-

siparis_rehberi= {  "Corbaci":"444 44 44",
                    "Pizza"  :"555 55 55",
                    "Kebapcı":"666 66 66" }
print "Sipariş Tipi : %s" %type(siparis_rehberi)   # veri tipinin ne olduğunu öğrenmek için.s
print siparis_rehberi
print "--------------"

sozluk={"Ad" :"Ahmet"}
print "Sozlukteki Ad in karsiligi : %s" %sozluk["Ad"]
sozluk["Soyad"]="Kara"
print sozluk["Soyad"]
sozluk["Yas"]=24
print sozluk["Yas"]
print type(sozluk["Yas"])
siparis_rehberi= {   "Corbaci":"444 44 44",
                     "Pizza"  :"555 55 55",
                     "Kebapci":"666 66 66" }
siparis_rehberi["Corbaci"]="777 77 77"
print siparis_rehberi

print  siparis_rehberi.keys()
print siparis_rehberi.values()
print "Tost Var mı  :",siparis_rehberi.has_key("Tost")
print "Pizza Var mı :",siparis_rehberi.has_key("Pizza")
print type(siparis_rehberi.get("Tost"))

    