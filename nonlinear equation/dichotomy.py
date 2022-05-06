import numpy as np
def func(x):
    return np.sin(x)
def dic(a,b,e):## 区间（a，b）上的根，e是精度
    while func(a)*func(b)<=0 and abs(a-b)>10e-5:
        c=(a+b)/2
        print('c=',c)
        if func(c)*func(b)<=0:
            a=c
        else:
            b=c
dic(-1,1,10e-5)
