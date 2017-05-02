from qtcarcas import Drawer
from math import sqrt, sin, cos, tan
from PyQt4 import QtCore
from bh import bresenham


class KGG3DDrawer(Drawer):
    def __init__(self, func):
        super().__init__()
        self.size = None
        self.func = func
        self.pxls = []
        self.fls = []

    def draw(self, qp):
        self.f2(qp)
        self.f2(qp, reverse=True)
        self.cleanup2(qp)

    def init_pxls(self):
        w = self.size.width()
        if len(self.pxls) < w:
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

    def cleanup2(self, qp):
        xx = 0
        for col in self.pxls:
            try:
                top_p = min(self.fls[0][xx] + self.fls[1][xx])
                bot_p = max(self.fls[0][xx]+self.fls[1][xx])
            except:
                continue
            for yy in col:

                if col[yy] == 'r' and yy < bot_p:
                    self.draw_point(qp, xx, yy, QtCore.Qt.white)
                if col[yy] == 'b' and yy > top_p:
                    self.draw_point(qp, xx, yy, QtCore.Qt.white)
            xx += 1

    def f2(self, qp, reverse=False):
        x1 = -2
        x2 = 4
        y1 = -3
        y2 = 5
        n = 75
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
                xx, yy = self.get_point_dimetry(x, y, z)
                if xx > maxx:
                    maxx = xx
                if yy > maxy:
                    maxy = yy
                if xx < minx:
                    minx = xx
                if yy < miny:
                    miny = yy

        for i in range(0, n + 1):
            last_bot = (None, None)
            last_top = (None, None)
            line = [list() for x in range(self.size.width())]
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

                xx, yy = self.get_point_dimetry(x, y, z)
                xx = int((xx - minx) / (maxx - minx) * self.size.width())
                yy = int((yy - miny) / (maxy - miny) * self.size.height())
                middle = True
                if xx >= self.size.width():
                    continue
                if yy > bottom[xx]:
                    # self.draw_point(qp, xx, yy, QtCore.Qt.red)
                    self.brez(qp, (xx, yy), last_bot, QtCore.Qt.red)
                    if i == 0:
                        line[xx].append(yy)
                    bottom[xx] = yy
                    last_bot = (xx, yy)
                    last_top = (None, None)
                    middle = True

                if yy < top[xx]:
                    # self.draw_point(qp, xx, yy, QtCore.Qt.blue)
                    self.brez(qp, (xx, yy), last_top, QtCore.Qt.blue)
                    if i == 0:
                        line[xx].append(yy)
                    top[xx] = yy
                    last_top = (xx, yy)
                    last_bot = (None, None)
                    self.pxls[xx][yy] = 'b'
                    middle = True

                if middle:
                    last_bot = (None, None)
                    last_top = (None, None)
            if i == 0:
                self.fls.append(line)

    @staticmethod
    def get_point_dimetry(x, y, z):
        return -x / (2 * sqrt(2)) + y, x / (2 * sqrt(2)) - z

    def brez(self, qp, p1, p2, color):
        if p2[0] is None and p2[1] is None:
            self.draw_point(qp, p1[0], p1[1], color)
            return
        qp.setPen(color)
        for p in bresenham(p1, p2):
            self.draw_point(qp, p[0], p[1], color)

    def remember_pixel(self, x, y, color):
        if color == QtCore.Qt.blue:
            self.pxls[x][y] = 'b'
        if color == QtCore.Qt.red:
            self.pxls[x][y] = 'r'

    def draw_point(self, qp, x, y, color):
        qp.setPen(color)
        qp.drawPoint(x, y)
        self.remember_pixel(x, y, color)
