import numpy as np
import matplotlib.pyplot as plt
A=[[-1,-6],[1,0],[2,6]]
def diff(A):
    A=np.array(A,dtype=float)
    n=A.shape[0]
    a=[A[i,1] for i in range(n)]
    for j in range(1,n):
        for i in range(n-1,j-1,-1):
            a[i]=(a[i]-a[i-1])/(A[i,0]-A[i-j,0])
    return a
def newton(A,x):
    m=A.shape[0]
    a=diff(A)
    sum,pr=a[0],1.0
    for i in range(1,m):
        pr=pr*(x-A[i-1,0])
        sum=sum+a[i]*pr
    return sum
def Newton(A):
    A=np.array(A,dtype=float)
    M,m=np.max(A[:,0]),np.min(A[:,0])
    xis=np.linspace(m,M,round((M-m)*1000))
    print(M,m)
    yis=[newton(A,xis[i]) for i in range(len(xis))]
    plt.scatter(A[:,0],A[:,1],color="b")
    plt.plot(xis,yis,color="r");plt.show()
A=[[1.765,0.92256],[1.760,0.92137],[1.755,0.92021],[1.750,0.91906]]
A=np.array(A,dtype=float)
Newton(A)
