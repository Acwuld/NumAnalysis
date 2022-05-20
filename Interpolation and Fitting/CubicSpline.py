from scipy import linalg 
def CubicSpline(x,y,ydd,xi):
    n=len(x)
    h,lam,mu=np.zeros(n),np.ones(n),np.ones(n)
    M,d=np.zeros(n),np.zeros(n)
    for i in range(1,n):
        h[i]=x[i]-x[i-1] 
    for i in range(1,n-1):
        lam[i]=h[i+1]/(h[i]+h[i+1]) #- lam[0]=$lam[1] lam[n-2]=$lam[n-1] 
        mu[i]=1-lam[i]
        d[i]=6/(h[i]+h[i+1])*((y[i+1]-y[i])/h[i+1]-(y[i]-y[i-1])/h[i])
    d[0]=6/h[1]*((y[1]-y[0])/h[1]-ydd[0])
    d[n-1]=6/h[n-1]*(ydd[1]-(y[n-1]-y[n-2])/h[n-1])
    A=2*np.eye(n)
    for i in range(n-2):
        A[i,i+1]=lam[i]
        A[i+1,i]=mu[i+1]
    M=linalg.solve(A,d)
    for i in range(1,n):
        if x[i-1]<=xi and xi<=x[i]:
            anw=(M[i-1]/6/h[i]*(x[i]-xi)**3+M[i]/6/h[i]*(xi-x[i-1])**3
            +1/h[i]*(y[i]-M[i]*h[i]**2/6)*(xi-x[i-1])+1/h[i]*(y[i-1]-M[i-1]*h[i]**2/6)*(x[i]-xi))
            return anw 
