import numpy as ny
def GAUSS(A,b):
    A,b=ny.array(A,dtype=float),ny.array(b,dtype=float)
    n=A.shape[0]
    b=b.reshape(n,1)
    A=ny.c_[A,b]
    for k in range(n):
        a=A[k:n,k]
        a=ny.abs(a)
        dt=ny.max(a,axis=0)
        t=ny.argmax(a,axis=0)
        if dt>a[0]:
            A[(k,t+k),:]=A[(t+k,k),:]
        for t in range(k,n-1):
            A[(t+1),:]=A[(t+1),:]-A[k,:]*A[(t+1),k]/A[k,k]
    x,s=ny.zeros(n),ny.zeros(n+1)
    for k in range(n-1,-1,-1):
        x[k]=(A[k,n]-s[k+1])/A[k,k]
        if ny.abs(x[k])<1.0e-10:#极小化为0
            x[k]=0
        if k>=1:
            for i in range(k,n):
                s[k]=s[k]+A[k-1,i]*x[i]
    return x.reshape(n,1)
A=[[4,2,-3,-1,2,1,0,0,0,0],
    [8,6,-5,-3,6,5,0,1,0,0],
    [4,2,-2,-1,3,2,-1,0,3,1],
    [0,-2,1,5,-1,3,-1,1,9,4],
    [-4,2,6,-1,6,7,-3,3,2,3],
    [8,6,-8,5,7,17,2,6,-3,5],
    [0,2,-1,3,-4,2,5,3,0,1],
    [16,10,-11,-9,17,34,2,-1,2,2],
    [4,6,2,-7,13,9,2,0,12,4],
    [0,0,-1,8,-3,-24,-8,6,3,-1]]
B=[5,12,3,2,3,46,13,38,19,-21]
print(GAUSS(A,B))
