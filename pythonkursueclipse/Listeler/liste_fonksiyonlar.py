# -*- coding: utf-8 -*-

print "Liste Tipinde kullannilabilecek Fonksiyonlar : "
print "append , remove , del , pop , reverse , sort , index , count"

dizim    =  [1,"ab",2,"cd",3,"ef",4,"gh",5]

print dizim

dizim.reverse()
print "\n dizim.reverse :", dizim
dizim.sort()
print dizim

sozlugum={"ad":"kadir","soyad":"koyici","yas":"33"}

print sozlugum

del sozlugum["yas"]

print "\n del liste :  ",sozlugum

takimlar = ['Galatasaray','Fenerbahçe','Beşiktaş']
takimlar.pop(2)
print takimlar

takimlar = ['Galatasaray','Fenerbahçe','Beşiktaş']
print takimlar.index('Galatasaray')

takimlar = ['Galatasaray','Fenerbahçe','Beşiktaş']
print "Bursaspor kaç tane geçiyor : ",takimlar.count('Bursaspor')


'''
def denemefonk():
    print "deneme"
    
takimlar = ['a','b','c',denemefonk,7,8,9]
 
takimlar.append('d')
takimlar.append('e')
takimlar.append('f')

#liste_adi.remove("eleman adi") 
takimlar.remove('e')    # liste adına göre silme islemi

del takimlar[len(takimlar)-1]         # indis numarasına göre silme işlemi

print takimlar

takimlar.remove(denemefonk)

print takimlar
takimlar.remove(8)
print takimlar
takimlar.reverse()
print takimlar

takimlar = ['Galatasaray','Fenerbahçe','Beşiktaş']
takimlar.pop(1)
print takimlar

takimlar.sort()
print takimlar

'''