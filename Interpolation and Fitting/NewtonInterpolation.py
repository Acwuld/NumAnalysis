import numpy as np
import matplotlib.pyplot as plt
def Newton(A,*b):
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
    A=np.array(A,dtype=float)
    if len(b)!=3:
        M,m=np.max(A[:,0]),np.min(A[:,0])
        xis=np.linspace(m,M,round((M-m)*1000))
    else:
        xis=np.linspace(b[1],b[2],round((b[2]-b[1])*1000))
    yis=[newton(A,xis[i]) for i in range(len(xis))]
    if len(b)!=0:
        print('F({})={}'.format(b[0],newton(A,b[0])))
    plt.scatter(A[:,0],A[:,1],color="b")
    plt.plot(xis,yis,color="r");plt.show()
A=np.array([[0.4,0.41075],[0.55,0.57815],[0.65,0.69675],[0.80,0.90],[0.95,1],[1.05,1.25382]])
Newton(A,0.99)
