double f(double x, double y) { 
    return cos(x*y);
}

double coord_x(double x, double y, double z) { 
    return (y-x)*sqrt(3.0)/2;
}

double coord_y(double x, double y, double z) {
    return (x+y)/2-z;
}

int main()
{
    int mx=800, my=600;
    initwindow(mx,my);
    double x,y,z,xx,yy,
    maxx,maxy,minx,miny,
    x1=-3,x2=3,y1=-3,y2=3;
    int i, j, n=50, m=mx*2;
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
        for (int j=0; j<=m; ++j) {
            y=y2+j*(y1-y2)/m;
            z=f(x,y);
            xx=coord_x(x,y,z);
            yy=coord_y(x,y,z);
            xx=(xx-minx)/(maxx-minx)*mx;
            yy=(yy-miny)/(maxy-miny)*my;
            if (yy>bottom[xx]) { 
                putpixel(xx,yy,1);
                bottom[xx]=yy; 
            }
            if (yy<top[xx]) { 
                putpixel(xx,yy,3);
                top[xx]=yy; 
            }
        }
    }
}