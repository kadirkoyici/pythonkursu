# -*- coding: utf-8 -*-

import sys
print sys.getdefaultencoding()
 
print "�ki Say�n�n B�l�m�"
 
sayi1=int(raw_input("Birinci Say�:"))
sayi2=int(raw_input("�kinci Say�:"))
try:
    bolum=float(sayi1/sayi2)
    print bolum        
except (ZeroDivisionError,ValueError):
    pass
print "Programdaki Hata G�sterilmiyor!"