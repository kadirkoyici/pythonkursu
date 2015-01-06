# -*- coding: utf-8 -*-
boskume=()
print boskume, "  " ,type(boskume)
'''
kume=set(["roman","oyku","hikaye","deneme"],["a",7],6,"dfgdf")  
Hata alırız -> TypeError: set expected at most 1 arguments, got 4
'''
liste=["roman","oyku","hikaye","deneme"]
kume1=set(["roman",5,"oyku",7,"hikaye",9,"deneme"])
print kume1, type(kume1)
kume2=set(liste)
print kume2, type(kume2) 

demet=("roman",5,"oyku",7,"hikaye",9,"deneme")
kume3=set(demet)
print kume3, type(kume3)

liste1=range(1,15)
print "liste 1 : ", liste1
liste2=range(3,11)
print "liste 2 : ", liste2
a=set(liste1)
b=set(liste2)
c=a.intersection(b)
print type(c)
j=0
for i in set(c):
    j=j+1
    print j, " -> ", i, type(i)
print "---------------------------"
print j 

print "\n-----------"

liste=["roman", "oyku" , "hikaye" , "deneme" , "roman" , "hikaye","roman"]
print "liste : ",liste
print "liste kumesi : ", set(liste)
print "\n-----------"
for i in set(liste):
 print "%s listede %s kez geciyor."  %(i,liste.count(i))