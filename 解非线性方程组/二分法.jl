function bisection(f::Function,a,b,eps,N)
    n=1
    p=0
    while n<=N
        p=a+(b-a)/2
        if f(p)==0||abs(a-b)<eps
            return println("p is $p and the iteration number is $n")
        end
        if f(a)f(p)<0
            b=p
        else
            a=p
        end
        n=n+1
    end
    y=f(p)
    println("Method did not converge.The last iteration gives $p with function value $y")
end
bisection(x->x^5+2*x^3-5*x-2,0,2,10^(-4),20)
