#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import re
 
karakter = "python programlama dilini öğreniyorum."
print  "tipi : ",type(re.match("python",karakter))
print "döndürdüğü değer : ",re.match("python",karakter)
print "dödürdüğü değerin karşılığı : ",re.match("python",karakter).group()
print  "döndürdüğü değerde delphi kelimesi varmı : ",re.match("delphi",karakter)
print  "dizinin en başında programlama var mı : ",re.match("programlama",karakter)
#match() metodu karakter dizisinin sadece en başına bakar
print karakter.split()[0]=="python"
print karakter.split()[1]=="python"
print karakter.split()[2]=="python"
print karakter.split()[3]=="python"


kontrol = re.match("python",karakter)
print "tipi : ", type(kontrol)
for i in dir(kontrol):
    print   i
