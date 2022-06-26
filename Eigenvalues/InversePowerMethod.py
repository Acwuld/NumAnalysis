import numpy
def IPowerm(A,u,p,N):
    A,u,t,a=np.array(A,dtype=float),np.array(u,dtype=float),1,0
    A=np.linalg.inv(A)
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
            print("特征值",1/mu,"特征向量",u,"^T")
        if i==N-1 and abs(t)>p:
            print("这个矩阵可能不收敛")
            break
A=[[-1,2,1],[2,-4,1],[1,1,-6]]
u=[1,1,1]
IPowerm(A,u,10e-5,100)
