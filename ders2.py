#-*- coding: utf-8 -*-
'''
print 6*(1-2)
a=input("a sayisini giriniz : ")
print a
b=raw_input("b karakter dizisini giriniz : ")
print b
'''
def isim(a,b):
    print a,b
isim("kadir", "köyiçi")
isim("kadir köyiçi", 5)
isim(5, 5+6)
def yenisatir():
    print "\ndeneme\tdeneme"
yenisatir()
def carpma(a,b):
    print a ,"degeri ile", b, "değerinin carpimi = ", (a*b)
carpma(5, 6)
