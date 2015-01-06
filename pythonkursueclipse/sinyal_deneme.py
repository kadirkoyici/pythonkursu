# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: cp1254 -*-
 
from PyQt4.QtGui import *
from PyQt4.QtCore import *
  
app = QApplication([])
  
window = QWidget()
window.setWindowTitle('PythonDersleri.com')
txtLabel = QLabel('Python Dersleri')
btnButton = QPushButton('Değiştir')
  
  
def changeTxtLabel():
    txtLabel.setText('Python Öğreniyorum')
  
window.connect(btnButton, SIGNAL('pressed()'), changeTxtLabel)
  
dizayn = QHBoxLayout()
dizayn.addWidget(txtLabel)
dizayn.addWidget(btnButton)
  
window.setLayout(dizayn)
window.show()
app.exec_()
