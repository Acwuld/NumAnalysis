def Crout(a,c,d,b):
    a,b,c,d=ny.array(a,dtype=float),ny.array(b,dtype=float),ny.array(c,dtype=float),ny.array(d,dtype=float)
    n=ny.alen(a)
    aalpha=ny.zeros(n)
    bbeta=ny.zeros(n-1)
    dd=ny.zeros(n)
    for q in range(1,n):
        dd[q]=d[q-1]
    aalpha[0]=a[0]
    for i in range(0,n-1):
        bbeta[i]=c[i]/aalpha[i]
        aalpha[i+1]=a[i+1]-dd[i+1]*bbeta[i]
    y=ny.zeros(n)
    y[0]=b[0]/aalpha[0]
    for j in range(1,n):
        y[j]=(b[j]-dd[j]*y[j-1])/aalpha[j]
    x=ny.zeros(n)
    x[n-1]=y[n-1]
    for k in range(n-2,-1,-1):
        x[k]=y[k]-bbeta[k]*x[k+1]
    x=x.reshape(n,1)
    for p in range(n):
        if ny.abs(x[p])<1.0e-12:
            x[p]=0
    return x
a,b,c=ny.zeros(10),ny.zeros(9),ny.zeros(9)
for i in range(10):
    a[i]=4
for j in range(9):
    c[j],b[j]=-1,-1
d=[7,5,-13,2,6,-12,14,-4,5,-5]
print(Crout(a,b,c,d))
