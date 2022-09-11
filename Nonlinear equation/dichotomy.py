import numpy as np
def f(x):
    return np.sin(x)
def dic(func,a,b,e):
    while func(a)*func(b)<=0 and abs(a-b)>e:
        c=(a+b)/2
        print('c=',c)
        if func(c)*func(b)<=0:
            a=c
        else:
            b=c
dic(f,-1,1,10e-5)
