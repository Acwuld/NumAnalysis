function secant(f::Function,pzero,pone,eps,N)
    n=1
    p=0. # to ensure the value of p carries out of the
    # while loop
    while n<=N
        p=pone-f(pone)*(pone-pzero)/(f(pone)-f(pzero))
        if f(p)==0 || abs(p-pone)<eps
            return println("p is $p and the iteration number is $n")
        end
        pzero=pone
        pone=p
        n=n+1
    end
    y=f(p)
    println("Method did not converge.The last iteration gives $p with function value $y")
end
secant(x->cos(x)-x,0.5,1,10^(-4),20)
