import numpy as np
import matplotlib.pyplot as plt
A=[[0.4,0.41075],[0.55,0.57815],[0.65,0.69675],[0.80,0.90],[0.95,1],[1.05,1.25382]]
def Lagrange(A,*b): #=b至多为三维数组，(b[1],b[2])为区间长度，b[0]是计算f(b[0])
    A,a=np.array(A,dtype=float),np.zeros(2,dtype=float)
    def Larange_1(A,a):
            s,n=0.0,A.shape[0]
            for i in range(n):
                t=A[i,1]
                for j in range(n):
                    if i!=j:
                        t*=(a-A[j,0])/(A[i,0]-A[j,0])
                s+=t
            return s
    n=A.shape[0]
    a[0],a[1]=A[0,0]-(A[n-1,0]-A[0,0])/10,A[n-1,0]+(A[n-1,0]-A[0,0])/10
    plt.scatter(A[:,0],A[:,1],color='r')
    if len(b)!=3:
        x=np.linspace(a[0],a[1],round((a[1]-a[0])*100))
    else:
        x=np.linspace(b[1],b[2],round((b[2]-b[1])*100))
    s=[Larange_1(A,x[i]) for i in range(len(x))]
    if len(b)!=0:
        print("F({})={}".format(b[0],Larange_1(A,b[0])))
    plt.plot(x,s,color='b');plt.show()
#Lagrange(A) ##插值。然后在默认区间画图
Lagrange(A,0.596) ##在默认区间画图，并计算F(0.596)
#Lagrange(A,0.596,0.5,6) ##在[0.5,6]画图，并计算F(0.596)
