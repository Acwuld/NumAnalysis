import numpy as np
def PowerM(A,u,p,N): ## A矩阵，u迭代初始向量，p精度，N最大迭代次数
    A,u,t,a=np.array(A,dtype=float),np.array(u,dtype=float),1,0
    for i in range(N):
        u=A.dot(u)
        u1=abs(u)
        k=np.argmax(u1,axis=0)
        mu=u[k]
        if a!=0:
            t=mu-a
        a=mu
        u=u/mu
        if abs(t) >p :
            print("第",i+1,"次迭代")
            print("特征值",mu,"特征向量",u,"^T")
        if i==N-1 and abs(t)>p:
            print("这个矩阵可能不收敛")
            break
A=[[2,1,3,4],[1,-3,1,5],[3,1,6,-2],[4,5,-2,-1]]
u=[1,1,1,1]
PowerM(A,u,10e-5,1500)
