# !/usr/bin/env python
# -*- coding: cp1254 -*-
 
from PyQt4.QtGui import *
 
uygulama = QApplication([])
etiket1 = QLabel('Merhaba PyQt')
etiket2 = QLabel('<font color="red" size="6">Merhaba PyQt</font>')

etiket1.show()
etiket2.show()


 
pencere = QWidget()

pencere.resize(300, 100) # Yeni boyutlar
pencere.move(50, 50) # Sol �st k��eden uzakl�k

etiket3 = QLabel('PythonDersleri.com')
buton = QPushButton('Butonum')
 
yatayKutu = QHBoxLayout()
yatayKutu.addWidget(etiket3)
yatayKutu.addWidget(buton)
 
pencere.setLayout(yatayKutu)
pencere.setWindowTitle('Program�m')
pencere.show()
 
uygulama.exec_()