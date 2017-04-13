from qtcarcas import Drawer
from math import sqrt, sin, cos, tan
from PyQt4 import QtCore

class KGG3DDrawer(Drawer):
    def __init__(self, func):
        super().__init__()
        self.size = None
        self.func = func

    def draw(self, qp):
        self.f2(qp)

    def f2(self, qp):
        x1 = -3
        x2 = 3
        y1 = -3
        y2 = 3
        n = 100
        miny = minx = 100000
        maxy = maxx = -minx
        top = [self.size.height()]*(self.size.width()+1)
        bottom = [0]*(self.size.width()+1)
        for i in range(0, n+1):
            x = x2 + i * (x1 - x2) / n
            for j in range(0, n):
                y = y2 + j * (y1 - y2) / n
                z = self.func(x, y)
                xx, yy = self.get_point_dimetry(x, y, z)
                if xx > maxx:
                    maxx = xx
                if yy > maxy:
                    maxy = yy
                if xx < minx:
                    minx = xx
                if yy < miny:
                    miny = yy

        for i in range(0, n+1):
            x = x2 + i * (x1 - x2) / n
            for j in range(self.size.width()*2 + 1):
                y = y2 + j * (y1 - y2) / (self.size.width() * 2)
                z = self.func(x, y)
                xx, yy = self.get_point_dimetry(x, y, z)
                xx = int((xx - minx) / (maxx - minx) * self.size.width())
                yy = int((yy - miny) / (maxy - miny) * self.size.height())
                print(xx, yy)
                if yy > bottom[xx]:
                    self.draw_point(qp, xx, yy, QtCore.Qt.red)
                    bottom[xx] = yy

                if yy < top[xx]:
                    self.draw_point(qp, xx, yy, QtCore.Qt.blue)
                    top[xx] = yy
            

    @staticmethod
    def get_point_dimetry(x, y, z):
        return (y-x)*sqrt(3.0)/2, (x+y)/2-z
        # return -x/(2*sqrt(2)) + y, x/(2*sqrt(2)) - z

    def draw_point(self, qp, x, y, color):
        qp.setPen(color)
        qp.drawPoint(x, y)
