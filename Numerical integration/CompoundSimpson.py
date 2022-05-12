import numpy as np
def comSimpson(f,a,b,n):
    h=(b-a)/n
    xi=np.array([a+(i+1)*h for i in range(n)])
    sum=f(a)+f(b)
    for i in range(1,n,2):
        sum=sum+4*f(xi[i])
    for i in range(2,n,2):
        sum=sum+2*f(xi[i])
    return (sum*h/3)
def f(x):
    if x==0: return 1
    else: return np.sin(x)/x
print(comSimpson(f,0,1,20))
