# -*- coding: utf-8 -*-
def faktoriyel(sayi1,sayi2):
    '''
    reduce() fonksiyonun içerisinde çağrılan fonksiyon iki argüman alır. 
    Bu argümanlar ilk önce listenin ilk iki elemanıdır. 
    Daha sonra dönen sonuç ve üçüncü elemanı, dönen sonuç ve dördüncü elemanı şeklinde devam eder. 
    reduce fonksiyonu geriye bir liste döndürmez. 
    Geri tek bir sonuç döner. Örneğin bu şekilde 10 sayısının faktoriyelini hesaplayabiliriz. 
    '''
    return sayi1*sayi2

sayilar = range(1,5)
print sayilar
print reduce(faktoriyel,sayilar)

def toplam_bul(i,j):    return i+j
k=range(1,8)
print k
print reduce(toplam_bul, k)