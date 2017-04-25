import math, tkinter


def f(x, y):
    return math.cos(x * y)


def coord_x(x, y, z, rev=False):
    if rev:
        x, y = y, x
    return -x / (2 * math.sqrt(2)) + y


def coord_y(x, y, z, rev=False):
    if rev:
        x, y = y, x
    return x / (2 * math.sqrt(2)) - z


def main(reverse=False):
    mx = 800
    my = 600
    x1 = -3
    x2 = 3
    y1 = -3
    y2 = 3
    n = 100
    m = mx * 2
    top = [my] * mx
    bottom = [0] * mx
    miny = minx = 10000
    maxy = maxx = -minx
    i = 0
    while i <= n:
        x = x2 + i * (x1 - x2) / n
        j = 0
        while j <= n:
            y = y2 + j * (y1 - y2) / n
            z = f(x, y)
            xx = coord_x(x, y, z, rev=reverse)
            yy = coord_y(x, y, z, rev=reverse)
            if xx > maxx:
                maxx = xx
            if yy > maxy:
                maxy = yy
            if xx < minx:
                minx = xx
            if yy < miny:
                miny = yy
            j += 1
        i += 1

    #    i=0
    #   while i < mx:
    #      top[i]=my
    #     bottom[i]=0
    #    i += 1

    i = 0
    while i <= n:
        x = x2 + i * (x1 - x2) / n
        j = 0
        while j <= mx * 2:
            y = y2 + j * (y1 - y2) / (mx * 2)
            z = f(x, y)
            xx = coord_x(y, x, z, rev=reverse)
            yy = coord_y(y, x, z, rev=reverse)

            xx = int((xx - minx) / (maxx - minx) * mx)
            yy = int((yy - miny) / (maxy - miny) * my)
            if xx >= mx:
                j += 1
                continue
            if yy > bottom[xx]:
                putpixel(xx, yy, 'red')
                bottom[xx] = yy
            if yy < top[xx]:
                putpixel(xx, yy, 'blue')
                top[xx] = yy
            j += 1
        i += 1


def putpixel(x, y, c):
    canv.create_oval(x, y, x, y, outline=c)


w = 800
h = 600
win = tkinter.Tk()
canv = tkinter.Canvas(win, height=h, width=w)
# xMax = GetSystemMetrics(0)
# yMax = GetSystemMetrics(1)
main()
main(True)
canv.pack()
win.mainloop()
