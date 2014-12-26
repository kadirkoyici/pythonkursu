# -*- coding: utf-8 -*-
#print """
print 'Pyhton\'da karakter dizileri (string) çalışıyoruz.'
'''
a=""
for i in range(10):
    a+=str(i)
    print i
    print a
'''
import os 

print "Kullanici Adi : " , os.environ["USERNAME"]
print "Bilgisayar Adı: " , os.environ["COMPUTERNAME"]
print "Ev dizini:      " , os.environ["HOMEPATH"]
print "İşlemci:        " , os.environ["PROCESSOR_IDENTIFIER"]
print "İşlemci sayısı: " , os.environ["NUMBER_OF_PROCESSORS"]
print "İşletim sistemi:" , os.environ["OS"]

a = u"Python öğreniyoruz."
print a[2:10:2]

