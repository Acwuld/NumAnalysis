def Larange_1(A,a):
    A=np.array(A,dtype=float)
    s,n=0.0,A.shape[0]
    for i in range(n):
        t=A[i,1]
        for j in range(n):
            if i!=j:
                t*=(a-A[j,0])/(A[i,0]-A[j,0])
        s+=t
    return s
A=[[0.4,0.41075],[0.55,0.57815],[0.65,0.69675],[0.80,0.90],[0.95,1],[1.05,1.25382]]
print(Larange_1(A,0.596))
