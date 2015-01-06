# -*- coding: utf-8 -*-
import os
for i in dir(os):
    print i
print "\n dir den donen deger : ",type(os.system("dir"))
print "sistem adi : ",os.name,type(os.name)
print "os.listdir : ",os.listdir("."), type(os.listdir("."))
print os.path.exists("C:\\")
print "os.path.basename() : ", os.path.basename("C:\\AMD\\Support\\12-8_vista_win7_win8_64_dd_ccc_whql")
print "os.path.dirname() : ", os.path.dirname("C:\\AMD\\Support\\12-8_vista_win7_win8_64_dd_ccc_whql")
print "os.path.splitext()",os.path.splitext("C:\\AMD\\Support\\12-8_vista_win7_win8_64_dd_ccc_whql\\Setup.exe"),type(os.path.splitext("C:\\AMD\\Support\\12-8_vista_win7_win8_64_dd_ccc_whql\\Setup.exe"))
print "os.path.join() : ",os.path.join("C:\\","Python27","python.exe"),type(os.path.join("C:","Python27","python.exe"))
print "os.path.abspath()", os.path.abspath("C:\\Python27\\python.exe")