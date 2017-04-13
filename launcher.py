import kggfunc
from PyQt4 import QtGui
import sys
from drawer import KGG3DDrawer
from qtcarcas import Carcass


def main():
    app = QtGui.QApplication(sys.argv)
    x = kggfunc.mf
    ex = Carcass(KGG3DDrawer(x))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
