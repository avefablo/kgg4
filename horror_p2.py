import math, tkinter


def f(x, y):
    return math.cos(x*y)

def coord_x(x, y, z):
    return -x/(2*math.sqrt(2)) + y
    #return (y-x)*math.sqrt(3)/2

def coord_y(x, y, z):
    return x/(2*math.sqrt(2)) - z
    #return (x+y)/2-z

def main():
    mx = 800
    my = 600
    x1 = -3
    x2 = 3
    y1 = -3
    y2 = 3
    n = 125
    m = mx*2
    top = [my] * (mx)
    bottom = [0] * (mx)
    miny = minx = 10000
    maxy = maxx = -minx
    i = 0
    while i <= n:
        x = x2 + i * (x1 - x2) / n
        j=0
        while j <= n:
            y=y2+j * (y1-y2) / n
            z=f(x, y)
            xx=coord_x(x, y, z)
            yy=coord_y(x, y, z)
            if (xx > maxx):
                maxx=xx
            if (yy > maxy):
                maxy=yy
            if (xx < minx):
                minx=xx
            if (yy < miny):
                miny=yy
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
        j=0
        while j <= mx*2:
            y=y2+j * (y1-y2) / mx*2
            z=f(x, y)
            xx=coord_x(x, y, z)
            yy=coord_y(x, y, z)
            xx= int((xx-minx) /(maxx-minx) * mx)
            yy= int((yy-miny) /(maxy-miny) * my)
           # if xx >= mx:
            #    continue
            print((len(bottom), xx))
            if (yy > bottom[xx]):
                putpixel(xx, yy, 1)
                bottom[xx]=yy
            if (yy < top[xx]):
                putpixel(xx, yy, 3)
                top[xx]=yy
            j += 1
        i += 1

def putpixel(x, y, c):
    canv.create_oval(x, y, x+1, y+1)

x = 800
y = 600
win = tkinter.Tk()
canv = tkinter.Canvas(win, height=y, width=x)
#xMax = GetSystemMetrics(0)
#yMax = GetSystemMetrics(1)
main()
canv.pack()
win.mainloop()
