# -*- coding: utf-8 -*-
print "clear pop popitem  items iteritems keys values copy fromkeys get  has_key setdefault update"

print "\nclear fonksiyonu : "
siparis_rehberi= { "Corbaci":"444 44 44",
                   "Pizza"  :"555 55 55",
                   "Kebapci":"666 66 66" }
print siparis_rehberi
print siparis_rehberi.clear()
print siparis_rehberi

print "\npop fonksiyonu"
siparis_rehberi={"Corbaci": "444 44 44" ,
                 "Pizza"  : "555 55 55" ,
                 "Kebapci": "666 66 66"}
print siparis_rehberi
print siparis_rehberi.pop("Corbaci")
print siparis_rehberi

print "\npopitem() fonksiyonu"
siparis_rehberi={"Corbaci": "444 44 44" ,
                 "Pizza"  : "555 55 55" ,
                 "Kebapci": "666 66 66"}
print siparis_rehberi.popitem()
print siparis_rehberi

print "\nitems() & iteritems() fonksiyonları"
siparis_rehberi={"Corbaci": "444 44 44" ,
                 "Pizza"  : "555 55 55" ,
                 "Kebapci": "666 66 66"}
print "items     : ", siparis_rehberi.items(), type(siparis_rehberi.items())
print "iteritems : ", siparis_rehberi.iteritems(), type(siparis_rehberi.iteritems())

print "\n -----------------------------"
for anahtar, deger in siparis_rehberi.items():
    print anahtar, deger, type(anahtar),type(deger)

print " -----------------------------\n"

print "\nkey fonksiyonu : "
siparis_rehberi= { "Corbaci" :"444 44 44",
                   "Pizza"   :"555 55 55",
                   "Kebapci" :"666 66 66" }
print  "keys : ",siparis_rehberi.keys()
print  "values : ",siparis_rehberi.values()

print "\ncopy fonksiyonu"
siparis_rehberi= { "Corbaci" :"444 44 44",
                   "Pizza"   :"555 55 55",
                   "Kebapci" :"666 66 66" }
yeni_siparis=siparis_rehberi.copy()
print "kopyalanmis yeni siparis : ", yeni_siparis

print "\nhas_key fonksiyonu , get ornegi"
siparis_rehberi= { "Corbaci" :"444 44 44",
                   "Pizza"   :"555 55 55",
                   "Kebapci" :"666 66 66" }

print "Tost Var mi ? : ",siparis_rehberi.has_key("Tost")
print "Pizza Var mi ? : ",siparis_rehberi.has_key("Pizza")

ara1="Tost"
print "siparis_rehberi icinde Tost arattigimizda : ",siparis_rehberi.get(ara1)
print siparis_rehberi.get(ara1, ara1+" Yok")

ara2="Pizza"

print siparis_rehberi.get(ara2, ara2+" Yok")

aranan=raw_input("Aradiginiz : ")
if siparis_rehberi.has_key(aranan):
    print aranan," Var", siparis_rehberi.get(aranan)
else :
    print aranan," Yok"












