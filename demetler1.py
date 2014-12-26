#!/usr/bin/env python
# -*- coding: utf-8 -*-
demet=()
print demet
print type(demet)

demet="Bir","Varmis",1,2,3,"Yokmus"
print demet

demetteklemanli=("tekeleman",)
print demetteklemanli
print type(demetteklemanli)

print "tek elemanli liste demet icinde sonunda virgul olmalidir"
demetteklemanlistevar=(["z","f",7,4,"c"],)
print type(demetteklemanlistevar)
demetteklemanlistevar=(["z","f",7,4,"c"])
print type(demetteklemanlistevar)
b=(["kavun", "karpuz", "cilek"],2,3,4,"beş")
print "0. elemanin 2. eleamni %s" %b[0][2]
b[0].append("muz")
print b[0]

c=("gh","fg","rr","nm",5,6)
print c.index("rr")

print "papatya kelimesinin 3. defa gectigi indisi ver"
d=("papatya","armut","papatya","meyve","cilek","papatya")
print d.index("papatya",3)
print d.count("papatya")
demetdegisken=(["kavun", "karpuz", "cilek"],2,3,4,"bes")
print "---------"
print demetdegisken

a,b,c,d,e=demetdegisken
print a,type(a)
print b,type(b)
print c,type(c)
print d,type(d)
print e,type(e)










