## 
import numpy as np
def Jacobi(A,b,x,a,N):## A系数矩阵,b向量,x初始迭代向量,a精度要求,N最大迭代次数
    A,b,x=np.array(A,dtype=float),np.array(b,dtype=float),np.array(x,dtype=float)
    n,t,nn=A.shape[0],1,0
    x0=np.zeros((n,1))
    b,x=b.reshape(n,1),x.reshape(n,1)
    for k in range(n):
        b[k]=b[k]/A[k,k]
    for i in range(n):
        A[i,:]=-A[i,:]/A[i,i]
    for j in range(n):
        A[j,j]=0
    while t>a:
        nn=nn+1
        x=np.dot(A,x)+b
        t=abs(max(x-x0))[0]
        x0=x
        if nn<=N:
            print("第{}次迭代,解向量x=\n{}\n,无穷范数|x_{{k+1}}-x{{k}}={}".format(nn,x,t))
        else:
            print("迭代次数已经超过{}了,请猜猜是否收敛".format(N))
            break
A=[[5,-1,-1,-1],[-1,10,-1,-1],[-1,-1,5,-1],[-1,-1,-1,10]]
B=[-4,12,8,34]
x0=np.zeros((1,4))
Jacobi(A,B,x0,0.001,100)            
