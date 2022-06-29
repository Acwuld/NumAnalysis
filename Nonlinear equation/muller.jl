function muller(f::Function,pzero,pone,ptwo,eps,N)
    n=1
    p=0
    while n<=N
        c=f(ptwo)
        b1=(pzero-ptwo)*(f(pone)-f(ptwo))/((pone-ptwo)*(pzero-pone))
        b2=(pone-ptwo)*(f(pzero)-f(ptwo))/((pzero-ptwo)*(pzero-pone))
        b=b1-b2
        a1=(f(pzero)-f(ptwo))/((pzero-ptwo)*(pzero-pone))
        a2=(f(pone)-f(ptwo))/((pone-ptwo)*(pzero-pone))
        a=a1-a2
        d=(Complex(b^2-4*a*c))^0.5
        if abs(b-d)<abs(b+d)
            inc=2c/(b+d)
        else
            inc=2c/(b-d)
        end
        p=ptwo-inc
        if f(p)==0||abs(p-ptwo)<eps
            return println("p is $p and the iteration number is $n")
        end
        pzero=pone
        pone=ptwo
        ptwo=p
        n=n+1
    end
    y=f(p)
    println("Method did not converage.The last iteration gives $p with function value $y")
end
muller(x->x^5+2x^3-5x-2,0.5,1.0,1.5,10^(-5),10)
muller(x->x^5+2x^3-5x-2,0.5,0,-0.1,10^(-5),10)
muller(x->x^5+2x^3-5x-2,0,-0.1,-1,10^(-5),10)
muller(x->x^5+2x^3-5x-2,5,10,14,10^(-5),20)
