function comsimpson(f::Function,a,b,n)
    h=(b-a)/n
    nodes =Array{Float64}(undef,n+1)
    for i in 1:n+1
        nodes[i] =a+(i-1)*h
    end
    sum=f(a)+f(b)
    for i in 3:2:n-1
        sum=sum+2*f(nodes[i])
    end
    for i in 2:2:n
        sum=sum+4*f(nodes[i])
    end
    return (sum*h/3)
end
comsimpson(x->x*log(x),1,2,12)
