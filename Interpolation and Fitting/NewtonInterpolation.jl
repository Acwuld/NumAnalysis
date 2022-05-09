using PyPlot
function diff(x::Array,y::Array)
    m=length(x)
    a=Array{Float64}(undef,m)
    for i in 1:m
        a[i]=y[i]
    end
    for j in 2:m
        for i in reverse(collect(j:m))
            a[i]=(a[i]-a[i-1])/(x[i]-x[i-(j-1)])
        end
    end
    return a
end
function newton(x::Array,y::Array,z)
    m=length(x)
    a=diff(x,y)
    sum,pr=a[1],1.0
    for j in 1:(m-1)
        pr=pr*(z-x[j])
        sum=sum+a[j+1]*pr
    end
    return sum
end
function Poltt(x::Array,y::Array)
    cla()
    M,m=max(x...),min(x...)
    t=(M-m)/10
    xaxis=m-t:1/1000:M+t
    yvals=map(t -> newton(x,y,t),xaxis)
    display(length(xaxis))
    plot(xaxis,yvals)
    scatter(x,y)
    gcf()
end
Poltt([1.765,1.760,1.755,1.750],[0.92256,0.92137,0.92021,0.91906])
