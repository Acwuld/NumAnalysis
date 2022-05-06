function newton(f::Function,fp::Function,pin,eps,N)## f=0,fp=f',pin=x0
    n,p=1,0
    while n<=N
        p=pin-f(pin)/fp(pin)
        if f(p)==0||abs(p-pin)<eps
            return println("p is $p and the iteration number is $n")
        end
        pin,n=p,n+1
    end
    y=f(p)
    println("Method did not converge.The last iteration gives $p with function value $y")
end
newton(x->x^5+2*x^3-5*x-2,x->5*x^4+6*x^2-5,1,10^(-4),20)
