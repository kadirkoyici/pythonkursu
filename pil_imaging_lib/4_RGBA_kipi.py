# -*- coding: utf-8 -*-
import Image
res=Image.open("rgba_example.png")
print res.mode
rr=res.load()
r,g,b,a=res.split()
r.save("./rgba_/r_.png") 
g.save("./rgba_/g_.png") 
b.save("./rgba_/b_.png") 
a.save("./rgba_/a_.png")
yeni=Image.merge("RGBA", (b, g, r, a))
yeni.save("yeni_rgba_example_png.png")

