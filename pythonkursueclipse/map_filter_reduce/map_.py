# -*- coding: utf-8 -*-
'''
map(function, sequence)
function have return
sequence is a list
'''
def kare(sayi):
    return sayi*sayi
sayilar = range(1,10)
print map(kare, sayilar),type(map(kare, sayilar))

def kucult(karakter):
    return karakter.lower()
kelimeler = ['SakarYa','PythoN','ProgramLama','FonksiYon','PythonDersleri','DjAngo']
print map(kucult,kelimeler)

def carp(sayi1,sayi2):
    return sayi1*sayi2
sayilar1 = range(1,10)
sayilar2 = range(11,20)
print map(carp,sayilar1,sayilar2) 

def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5,39)

F = map(fahrenheit, temp)
print temp,type(temp),F, type(F)
C = map(celsius, F)