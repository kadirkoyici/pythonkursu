# -*- coding: utf-8 -*-
import Image
print Image.VERSION
res=Image.open("python-logo.gif")
print type(res)
print res
print dir(res)
print "Format : ",res.format, "Çözünürlük : ",res.size, "Resim Kipi : ",res.mode
#res.show()
res.mode='RGB'
print "Format : ",res.format, "Çözünürlük : ",res.size, "Resim Kipi : ",res.mode
