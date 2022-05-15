def RungeKutta_1(f2,x0,y0,h):
    K1=f2(x0,y0)
    K2=f2(x0,y0+1/2*h*K1)
    K3=f2(x0+1/2*h,y0+1/2*h*K2)
    K4=f2(x0+h,y0+h*K3)
    X=[i/10 for i in range(10)]
    Y=[i/10 for i in range(10)]
    for i in range(10):
        X[i]=x0;Y[i]=y0;
        y=y0+h/6*(K1+2*K2+2*K3+K4)
        y0=y
        K1=f2(x0,y0)
        K2=f2(x0,y0+1/2*h*K1)
        K3=f2(x0+1/2*h,y0+1/2*h*K2)
        K4=f2(x0+h,y0+h*K3)
        x0=x0+h
        print("y({})={}".format(x0,y0))
    plt.plot(X,Y)
    plt.show()
def f2(x,y):#-y(-1)=0
    return x**2-y**2
RungeKutta_2(-1,0,0.1) #-y(-1)=0
