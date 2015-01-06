# -*- coding: utf-8 -*-
def teksayi(sayi):
    '''
    filter() fonksiyonu ise çağırılan fonksiyonun döndürdüğü değerin true olduğu durumlara göre liste döndürür
    Geriye Liste de döndürebilir Demet de döndürebilir.
    '''
    return sayi%2==1

liste = range(1,20)
teksayilar=filter(teksayi,liste)
print liste
print teksayilar
print teksayi.__doc__

print "--"*40
def baslik(karakter):
    return karakter.istitle()
liste = ['Python Dersleri','django','Python','Sakarya universitesi']
demet = ('Python Dersleri','django','Python','Sakarya universitesi')
print filter(baslik,liste),type(filter(baslik,liste))
print filter(baslik,demet),type(filter(baslik,demet))
