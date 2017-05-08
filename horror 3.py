import math, tkinter
from bresenham import  bresenham
from win32api import GetSystemMetrics


def coord_x(x, y, z):
    return (y-x) * math.sqrt(3) / 2


def coord_y(x, y, z):
    return (x + y) / 2 - z


def main(reverse):
    global W, H
    mx = W
    my = H
    n = 100
    top = [my] * mx
    bottom = [0] * mx
    minx = float('inf')
    miny = minx
    maxx = -minx
    maxy = maxx
    for i in range(n):
        if reverse:
            y = y2 + i * (y1 - y2) / n
        else:
            x = x2 + i * (x1 - x2) / n
        for j in range(n):
            if reverse:
                x = x2 + j * (x1 - x2) / n
            else:
                y = y2 + j * (y1 - y2) / n
            z = f(x, y)
            xx = coord_x(x, y, z)
            yy = coord_y(x, y, z)
            if xx > maxx:
                maxx = xx
            if yy > maxy:
                maxy = yy
            if xx < minx:
                minx = xx
            if yy < miny:
                miny = yy

    for i in range(n+1):
        last_bot = (None, None)
        last_top = (None, None)
        line = [list() for x in range(mx)]
        if reverse:
            y = y2 + i * (y1 - y2) / n
        else:
            x = x2 + i * (x1 - x2) / n
        for j in range(mx * 2):
            if reverse:
                x = x2 + j * (x1 - x2) / (mx * 2)
            else:
                y = y2 + j * (y1 - y2) / (mx * 2)
            z = f(x, y)
            xx, yy = coord_x(x, y, z), coord_y(x, y, z)
            xx, yy = int((xx - minx) / (maxx - minx) * mx), int((yy - miny) / (maxy - miny) * my)
            middle = True
            if xx >= mx:
                continue
            if yy >= bottom[xx]:
                brez((xx, yy), last_bot, 'slate grey')
                if i == 0:
                    line[xx].append(yy)
                bottom[xx] = yy
                last_bot = (xx, yy)
                last_top = (None, None)
                done[xx][yy] = 'g'
                middle = False
            if yy <= top[xx]:
                brez((xx, yy), last_top, 'dodger blue')
                if i == 0:
                    line[xx].append(yy)
                top[xx] = yy
                last_top = (xx, yy)
                last_bot = (None, None)
                done[xx][yy] = 'b'
                middle = False
            if middle:
                last_bot, last_top = (None, None), (None, None)

def cleanup():
    xx = 0
    for col in done:
        b = max(filter(lambda x: x[1] == 'b', col.items()))
        b = b[0]
        for pxl in filter(lambda x: x[1] == 'g', col.items()):
            if pxl[0] < b:
                putpixel(xx, pxl[0],'white')
        xx += 1


def brez(p1, p2, color):
   # print((p1, p2))
    if p2[0] is None and p2[1] is None:
        putpixel(p1[0], p1[1], color)
        return

    for p in bresenham(p1[0], p1[1], p2[0], p2[1]):
        putpixel(p[0], p[1], color)




def putpixel(x, y, c):
    canv.create_line(x, y, x+1, y+1, fill=c)


def f(x, y):
    return (math.sin(x * y)**2)


W = 800
H = 700

x1, x2 = (-2, 4)
y1, y2 = (-4, 2)

done = []
w = W
if len(done) < w:
    for i in range(w):
        done.append(dict())
win = tkinter.Tk()
canv = tkinter.Canvas(win, height=H, width=W, bg='white')

main(False)
main(True)
cleanup()
#main(True)
#print(done)
canv.pack()
win.mainloop()
