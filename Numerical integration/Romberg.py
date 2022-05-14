#有点问题未解决…
import numpy as np
def Romberg(f,a,b,e):
    n=6
    def T0(n):
        T=np.zeros(n,dtype=float)
        T[0]=(b-a)*(f(a)+f(b))/2
        for i in range(1,n):
            s=0
            for j in range(2**(i-1)):
                s=s+f(a+(2*j+1)*(b-a)/(2**i))
            T[i]=T[i-1]/2+(b-a)/2**i*s
        return T
    Ta=T0(n)
    print(Ta)
    def T1(T,k):
        m=len(T)
        for i in range(m-1):
            T[i]=(4**k*T[i+1]-T[i])/(4**k-1)
        T=np.delete(T,m-1)
        return T
    for k in range(1,n):
        N=len(Ta)
        for i in range(1,N):
            if abs(Ta[i]-Ta[i-1])<e:
                print(Ta[i]);break
        else:Ta=T1(Ta,k) 
def f5(x):
    return x**(3/2)
Romberg(f5,0,1,10e-5)
