## Jacobi的分量形式
import numpy as np
def Jacobi(A,b,x,e,N): ## Ax=b,e precision ,N max times 
    A,b=np.array(A,dtype=float),np.array(b,dtype=float)
    n=A.shape[0]
    x,y=np.array(x),np.zeros(n)
    for k in range(N):
        for i in range(n):
            m=0
            for j in range(n):
                m=m+A[i,j]*x[j]
            y[i]=x[i]+(b[i]-m)/A[i,i]
        R=max(abs(x-y))
        x=y.copy()       
        if R>e:
            print("第{}次迭代,解向量x=\n{}\n,无穷范数|x_{{k+1}}-x{{k}}|={}".format(k+1,y,R))
        else:
            print("第{}次迭代,解向量x=\n{}\n,无穷范数|x_{{k+1}}-x{{k}}|={}".format(k+1,y,R))
            break
A,b=[[5,-1,-1,-1],[-1,10,-1,-1],[-1,-1,5,-1],[-1,-1,-1,10]],[-4,12,8,34]
x0=np.zeros(4)
Jacobi(A,b,x0,10e-5,100)
