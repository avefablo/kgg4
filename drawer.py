from qtcarcas import Drawer
from math import sqrt, sin, cos, tan
from PyQt4 import QtCore




class KGG3DDrawer(Drawer):
    def __init__(self, func):
        super().__init__()
        self.size = None
        self.func = func
        self.pxls = []

    def draw(self, qp):
        self.f2(qp)
        self.f2(qp, reverse=True)
        #self.cleanup(qp)

    def init_pxls(self):
        w = self.size.width()
        if len(self.pxls) == 0:
            for i in range(w):
                self.pxls.append(dict())

    def cleanup(self, qp):
        xx = 0
        for col in self.pxls:
            b = max(filter(lambda x: x[1] == 'b', col.items()))
            b = b[0]
            for pxl in filter(lambda x: x[1] == 'r', col.items()):
                if pxl[0] < b:
                    self.draw_point(qp, xx, pxl[0], QtCore.Qt.white)
            xx += 1

    def f2(self, qp, reverse=False):
        x1 = -2
        x2 = 1
        y1 = -3
        y2 = 2
        self.x_shift = 1
        self.y_shift = 1
        n = 100
        miny = minx = 10000
        maxy = maxx = -minx
        top = [self.size.height()] * (self.size.width())
        bottom = [0] * (self.size.width())
        self.init_pxls()
        for i in range(0, n + 1):
            if reverse:
                y = y2 + i * (y1 - y2) / n
            else:
                x = x2 + i * (x1 - x2) / n
            for j in range(0, n):
                if reverse:
                    x = x2 + j * (x1 - x2) / n
                else:
                    y = y2 + j * (y1 - y2) / n
                z = self.func(x, y)
                xx, yy = self.get_point_dimetry(x, y, z, reverse)

                if xx > maxx:
                    maxx = xx
                if yy > maxy:
                    maxy = yy
                if xx < minx:
                    minx = xx
                if yy < miny:
                    miny = yy

        for i in range(0, n + 1):
            if reverse:
                y = y2 + i * (y1 - y2) / n
            else:
                x = x2 + i * (x1 - x2) / n
            for j in range(self.size.width() * 2 + 1):
                if reverse:
                    x = x2 + j * (x1 - x2) / (self.size.width() * 2)
                else:
                    y = y2 + j * (y1 - y2) / (self.size.width() * 2)
                z = self.func(x, y)

                xx, yy = self.get_point_dimetry(x, y, z, reverse)
                xx = int((xx - minx) / (maxx - minx) * self.size.width())
                yy = int((yy - miny) / (maxy - miny) * self.size.height())

                if xx >= self.size.width():
                    continue
                if yy > bottom[xx]:
                    self.draw_point(qp, xx, yy, QtCore.Qt.red)
                    if xx in self.pxls and self.pxls[xx][yy] == 'b':
                        continue
                    bottom[xx] = yy
                    self.pxls[xx][yy] = 'r'

                if yy < top[xx]:
                    self.draw_point(qp, xx, yy, QtCore.Qt.blue)
                    top[xx] = yy
                    self.pxls[xx][yy] = 'b'

    def get_point_dimetry(self, x, y, z, reverse):
        return -x / (2 * sqrt(2)) + y, x / (2 * sqrt(2)) - z

    @staticmethod
    def draw_point(qp, x, y, color):
        qp.setPen(color)
        qp.drawPoint(x, y)
