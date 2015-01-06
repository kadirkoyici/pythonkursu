# -*- coding: utf-8 -*-
import os
klasor = "."
for i in os.listdir(klasor):
    dosya = os.path.join(klasor,i)
    if os.path.isdir(dosya):
        print 'Klas�r => ',i
    elif os.path.isfile(dosya):
        print 'Dosya => ',i

#os.walk() fonksiyonu
print "\n  os.walk() \n Program içerisinde bir klasörün tüm alt klasörleri ile birlikte taranmasını sağlar"
print ". walk() iterasyon edilebilir bir nesnedir. İterasyon sonucunda 3 elemandan oluşan bir demet döner."
print " İlk eleman bulunulan klasörü, ikinci eleman bu klasörde bulunan klasörlerin listesi, üçüncü eleman ise bu klasörde bulunan dosyaların bir listesidir. \n"
for i in os.walk("."):
    print i        