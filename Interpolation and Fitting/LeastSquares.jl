using PyPlot
function leastsqfit(x::Array,y::Array,n)
    m=length(x)
    d=n+1
    A,b=zeros(d,d),zeros(d,1)
    p=Array{Float64}(undef,2*n+1)
    for k in 1:d
        sum=0
        for i in 1:m
            sum=sum+y[i]*x[i]^(k-1)
        end
        b[k]=sum
    end
    p[1]=m
    for i in 2:2*n+1
        sum =0
        for j in 1:m
            sum=sum+x[j]^(i-1)
        end
        p[i]=sum
    end
    for k in 1:d
        for j in k:d
            A[k,j]=p[k+j-1]
        end
    end
    for i in 2:d
        for j in 1:i-1
            A[i,j]=A[j,i]
        end
    end
    a=A\b
end
function poly(x,A::Array)
    d,sum=length(A),0
    for i in 1:d
        sum=sum+A[i]*x^(i-1)
    end
    return sum
end
function SSE(A::Array,x::Array,y::Array)
    m,sum=length(y),0
    for i in 1:m
        sum=sum+(y[i]-poly(x[i],a))^2
    end
    return sum
end
function Pollt(x::Array,y::Array,n)
    m=length(x)
    a=leastsqfit(xd,yd,n)
    xaxis=x[1]:1/100:x[m]
    yvals=map(x->poly(x,a),xaxis)
    plot(xaxis,yvals)
    scatter(x,y)
    gcf()
end
xd=[1,2,3,4,5,6]
yd=[3,5,9.2,11,14.5,19]
Pollt(xd,yd,1)
