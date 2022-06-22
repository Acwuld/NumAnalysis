import numpy as np
def trapezoid(f,a,b,N):
    h   = (b-a)/N
    xi  = np.linspace(a,b,N+1)
    fi  = [f(xi[i]) for i in range(N+1)]
    s   = 0.0
    for i in range(1,N):
        s = s + fi[i]
    s = (h/2)*(fi[0] + fi[N]) + h*s
    return s
def romberg(f,a,b,e,N):
    Q = np.zeros((N,N),float)
    for i in range(0,N):
        N= 2**i
        Q[i,0] = trapezoid(f,a,b,N)
        for k in range(0,i):
            n        = k + 2
            Q[i,k+1] = 1.0/(4**(n-1)-1)*(4**(n-1)*Q[i,k] - Q[i-1,k])
        if (i > 0):
            if (abs(Q[i,k+1] - Q[i,k]) < e):
               break
    print( Q[i,k+1],N )   
    return Q[i,k+1]
def f1(x):
    return np.sqrt(4-(np.sin(x))**2)
def f2(x):
   if x==0: return 1
   else: return np.sin(x)/x
def f3(x):
   return np.exp(x)/(4+x**2)
def f4(x):
    return np.log(1+x)/(1+x**2)
romberg(f1,0,0.25,1.0e-12,10)
romberg(f2,0,1,1.0e-12,10)
romberg(f3,0,1,1.0e-12,10)
romberg(f4,0,1,1.0e-12,10)
#Romberg
#g = lambda x: 1/np.sqrt(np.pi) * np.exp(-x**2)
#result = integrate.romberg(g, 0, 1, show=True)
