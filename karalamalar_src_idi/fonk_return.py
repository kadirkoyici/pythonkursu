# -*- coding: utf-8 -*-

def gec():
    pass
 
def dondur(not_):
    if not_ > 50:
        return "Dersten Gectiniz."
    else:
        return "Dersten Kaldiniz."
 
notgir=int(raw_input("Aldiginiz Notu Giriniz : "))
sonuc = dondur(notgir)
print sonuc

def dondur2(sayi):
    return sayi % 2
 
sonuc = dondur2(notgir)
if sonuc==1:
    print "Sayı Tek."
else:
    print "Sayı Çift."
    
ucret = raw_input("Ücreti giriniz:")
 
if ucret>50:
    print "Bu ücrete kitap yoktur."
    gec()
else:
    print "Bu ücrete kitap bulabilirsiniz."
 
print "Teşekkürler"



 