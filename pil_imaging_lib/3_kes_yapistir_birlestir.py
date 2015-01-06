# -*- coding: utf-8 -*-
import Image
res=Image.open("tux-thinkpad.gif")
kutu=(60,6,250,196)
alan=res.crop(kutu)
alan.save('yeni_tux-thinkpad.gif')
ters=alan.rotate(180)
ters.save("yeni_tux-thinkpad.gif")

res.paste(alan, kutu)
res.save("ters-kafali-penguen.gif")