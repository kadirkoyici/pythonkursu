#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import re

python ="""Python, nesne yönelimli, yorumlanabilen, birimsel (modüler) ve etkileşimli bir programlama dilidir.
Girintilere dayalı basit sözdizimi, dilin öğrenilmesini ve akılda kalmasını kolaylaştırır.Bu
da ona söz diziminin ayrıntıları ile vakit yitirmeden programlama yapılmaya başlanabilen bir dil olma özelliği kazandırır.
Modüler yapısı, sınıf dizgesini (sistem) ve her türlü veri alanı girişini destekler. Hemen hemen her türlü platformda çalışabilir.
(Unix , Linux, Mac, Windows, Amiga, Symbian)... Python ... ile sistem programlama, kullanıcı arabirimi programlama, ağ programlama, uygulama ve veritabanı
yazılımı programlama gibi birçok alanda yazılım geliştirebilirsiniz. Büyük yazılımların hızlı bir şekilde prototiplerinin üretilmesi ve
denenmesi gerektiği durumlarda da C ya da C++ gibi dillere tercih edilir."""
 
kontrol=re.findall("Python",python);
print type(kontrol)
print kontrol, " liste döndürdü , uzunluğu : ", len(kontrol)