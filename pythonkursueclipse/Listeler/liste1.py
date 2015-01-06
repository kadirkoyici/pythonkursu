# -*- coding: utf-8 -*-
#cumle = ['hayat','python','ile','guzel']
#print "Listenin 2. elemani:", cumle[1]

liste3 = [1,2,3,4,5]
dizilen=len(liste3)

print " Liste elemanlari : ", liste3
print " Liste Uzunlugu : ",dizilen
print " Listenin son elemani  :", liste3[dizilen-1]
for i,v in enumerate(liste3):
    print i ," . eleman : ",v

print liste3[1:3] , liste3[:3],liste3[1:], liste3[1::2]

for i in range(0,dizilen):
    j=(dizilen-i)-1
    print j , " : ",liste3[0:j+1]
print liste3[1::2]

for i in range(0,dizilen):
    liste3.append("a")
print liste3
'''
for i in range(1,10,3): # 1 , 4 , 7
    print i
    '''
