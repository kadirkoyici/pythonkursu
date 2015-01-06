#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
for i in dir(os):
    print i
print "----------------"
print os.name

if os.system("mkdir 'YeniKlasor'"):
    print "Klasor Basarili Bir Sekilde Olusturuldu."
else:
    print "Klasor Olusturulamadi."

os.system("notepad yazi.txt")
os.startfile("yazi.txt")
print os.listdir(".")

for i,k in enumerate(os.listdir(".")):
    print i+1,k

print os.path.exists('C:\Users\Kadir\workspace\denemepydev\src\deneme\ddd')    
print os.path.exists('C:\Users\Kadir\workspace\denemepydev\src\deneme\altklasor1')    

for i in os.walk("C:\Users\Kadir\workspace"):
    print i
print os.getcwd()
print os.sep
