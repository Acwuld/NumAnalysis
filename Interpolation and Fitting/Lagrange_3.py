import numpy as np
import matplotlib.pyplot as plt
def Lagrange(A,B,*b): #=b至多为三维数组，(b[1],b[2])为区间长度，b[0]是计算f(b[0])
    A,B=np.array(A,dtype=float),np.array(B,dtype=float)
    def Larange_1(A,a):
            s,n=0.0,A.shape[0]
            for i in range(n):
                t=A[i,1]
                for j in range(n):
                    if i!=j:
                        t*=(a-A[j,0])/(A[i,0]-A[j,0])
                s+=t
            return s
    n,a=A.shape[0],np.zeros(2,dtype=float)
    a[0],a[1]=A[0,0]-(A[n-1,0]-A[0,0])/10,B[n-1,0]+(B[n-1,0]-B[0,0])/10
    plt.scatter(A[:,0],A[:,1],color='r')
    plt.scatter(B[:,0],B[:,1],color='b')
    Ax=np.linspace(a[0],A[n-1,0],round((A[n-1,0]-a[0])*100))
    Bx=np.linspace(B[0,0],a[1],round((a[1]-B[0,0])*100))
    s=[Larange_1(A,Ax[i]) for i in range(len(Ax))]
    p=[Larange_1(B,Bx[i]) for i in range(len(Bx))]
    if b:
        if A[0,0]<=b <=A[n-1,0]:
            print("F({})={}".format(b[0],Larange_1(A,b[0])))
        if B[0,0]<=b <=B[n-1,0]:
            print("F({})={}".format(b[0],Larange_1(B,b[0])))
    plt.plot(Ax,s,color='deeppink')
    plt.plot(Bx,p,color='chartreuse')
    plt.show()
A=[[0.4,0.41075],[0.55,0.57815],[0.65,0.69675]]
B=[[0.65,0.69675],[0.80,0.90],[0.95,1]]
#-Lagrange(A,B)
Lagrange(A,B,0.596)
