#include <cmath>
#include <iostream>
using namespace std;

double f(double x, double y) { 
    return cos(x*y);
}

double coord_x (double x, double y, double z) { 
    return  -x/(2*sqrt(2)) + y;
}

double coord_y (double x, double y, double z) {
    return x/(2*sqrt(2)) - z;
}

int main()
{
    int mx=800, my=600;
    double x,y,z,xx,yy, maxx,maxy,minx,miny, x1=-3,x2=3,y1=-3,y2=3;
    int xxt, yyt;
    int i, j, n=100, m=mx*2;
    int top[mx], bottom[mx];
    minx=10000; maxx=-minx;
    miny=minx; maxy=maxx; 
    for (int i=0; i<=n; ++i) { 
        x=x2+i*(x1-x2)/n;
        for (int j=0; j<=n; ++j) { 
            y=y2+j*(y1-y2)/n;
            z=f(x,y);
            xx=coord_x(x,y,z);
            yy=coord_y(x,y,z);
            if (xx>maxx) 
                maxx=xx;
            if (yy>maxy) 
                maxy=yy;
            if (xx<minx) 
                minx=xx;
            if (yy<miny) 
                miny=yy;
        } 
    }
    for (int i=0; i<mx; ++i) {
        top[i]=my; bottom[i]=0; 
    }
    for (int i=0; i<=n; ++i) {
        x=x2+i*(x1-x2)/n;
        cout << x << endl;
        for (int j=0; j<=m; ++j) {
            y=y2+j*(y1-y2)/m;
            cout << y << endl;
            z=f(x,y);
            xx=coord_x(x,y,z);
            yy=coord_y(x,y,z);
            xxt=(int)((xx-minx)/(maxx-minx)*mx);
            yyt=(int)((yy-miny)/(maxy-miny)*my);
            if (yy>bottom[xxt]) { 
                bottom[xxt]=yyt; 
            }
            if (yy<top[xxt]) { 
                top[xxt]=yyt; 
            }
        }
        break;
    }
}