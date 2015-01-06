# -*- coding: utf-8 -*-
 
def fonk():
    a="Global degiskenler"
    print a
fonk()
# print a global fonk icindeki degere  ulasilamaz NameError: name 'a' is not defined

print "------ global degiskenler ------"
def fonkg():
    global ag
    ag="Global değişkenler"
 
fonkg()
print ag