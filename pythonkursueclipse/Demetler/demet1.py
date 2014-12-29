# -*- coding: utf-8 -*-
print" Listeleri oluşturduktan sonra veri ekleyip çıkartabilirken \n demetlerde böyle bir şey yapamıyoruz. \n Zaten demet denmesinin sebebi de bu. \n demetler ekleme çıkarma gibi işlemlerle uğraşmadığı için daha hızlı çalışır \n ve eklenen verilerin program boyunca değiştirilmesini istemiyorsak \nçok işimize yarar."

bosdemet=() 
print bosdemet


def fonkeleman():
    print "demet icinde fonksiyon kullandik"

dizieleman=["cxv","fdf",3,4,fonkeleman]
a = (["kavun", "karpuz", "çilek"],) 
print a, "  " ,type(a)

demet1="Bir",1,fonkeleman,"Yokmus",2,dizieleman
print "\n demet1 tipi : ", type(demet1), " demet elemanlari : ", demet1 ,"\n" 

demet2=("\n Bir","Varmış",1,"Yokmuş",2,3)
print type(demet2)

demet3="tek",
print type(demet3)

demet4="",
print type(demet4)

demet5=("",)
print "demet5 tipi : ",type(demet5), "  " ,demet5