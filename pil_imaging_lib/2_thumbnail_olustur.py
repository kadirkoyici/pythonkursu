# -*- coding: utf-8 -*-
#!/usr/bin/python
import os
import Image
klasor='penguenler'
kucukler='penguenler_onizleme'
if not os.path.exists(kucukler):
    os.mkdir(kucukler)
for i in os.listdir(klasor):
    resim_dosyasi=klasor+'/'+i
    res=Image.open(resim_dosyasi)
    res.thumbnail((100, 100))
    res.save(kucukler+'/'+i)
    