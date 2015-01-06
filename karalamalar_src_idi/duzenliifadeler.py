#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import re
for i in dir(re):
    print " ----- ",i," ----- \n"
    a="re."+i
    print i," - >\n", help(a)
    print "------------------------------------\n"