#!/usr/bin/python3


from PyQt4 import QtGui
import sys
from drawer import KGG3DDrawer
from qtcarcas import Carcass
from math import cos, sin

def main():
    app = QtGui.QApplication(sys.argv)
    t = lambda x, y: sin(x * y) ** 2
    ex = Carcass(KGG3DDrawer(t))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
