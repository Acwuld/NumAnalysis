function HeavyIntegrationMonteCarloMethod(f::Function,a,b,c,d,n)
    sum = 0
    for i in 1:n
        sum = sum + f(a+(b-a)*rand(),c+(d-c)*rand())*(b-a)*(d-c)
    end
    return sum/n
end
# \int_0^1{\int_0^1{\left( \frac{\pi}{2}\sin \pi x \right) \left( \frac{\pi}{2}\sin \pi y \right)}}\mathrm{d}y\mathrm{d}x
HeavyIntegrationMonteCarloMethod((x,y) ->(π^2/4)*sin(π*x)*sin(π*y),0,1,0,1,5000)
