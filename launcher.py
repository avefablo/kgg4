#!/usr/bin/python3


from PyQt4 import QtGui
import sys
from drawer import KGG3DDrawer
from qtcarcas import Carcass
from math import cos, sin

def main():
    app = QtGui.QApplication(sys.argv)
    t = lambda x, y: cos(x*y)
    ex = Carcass(KGG3DDrawer(t))
    app.exec_()
    app.deleteLater()
    exit()

if __name__ == '__main__':
    main()
