import math, tkinter


def f(x, y):
    return math.sin(x * y) ** 2


def coord_x(x, y, z):
    return -x / (2 * math.sqrt(2)) + y


def coord_y(x, y, z):
    return x / (2 * math.sqrt(2)) - z


def main(reverse=False):
    mx = 800
    my = 600
    x1 = -2
    x2 = 4
    y1 = -4
    y2 = 2
    n = 100
    top = [my] * mx
    bottom = [0] * mx
    miny = minx = 1000000
    maxy = maxx = -minx
    
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


    for i in range (n):
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
            xx = coord_x(x, y, z)
            yy = coord_y(x, y, z)

            xx = int((xx - minx) / (maxx - minx) * mx)
            yy = int((yy - miny) / (maxy - miny) * my)
            if xx >= mx:
                continue
            if yy > bottom[xx]:
                putpixel(xx, yy, 'red')
                bottom[xx] = yy
            if yy < top[xx]:
                putpixel(xx, yy, 'blue')
                top[xx] = yy
  


def putpixel(x, y, c):
    canv.create_line(x, y, x+1, y+1, fill=c)


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
