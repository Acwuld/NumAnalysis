public class Dichotomy {
    public static void dichotomy(double a,double b,double e){
        double c ;
        while (Function.setF(a)*Function.setF(b)<=0&&Math.abs(a-b)>e){
            c=(a+b)/2;
            System.out.println("c="+c);
            if(Function.setF(c)*Function.setF(b)<=0){
                a=c;
            }else {
                b=c;
            }
    }
}

    public static void main(String[] args) {
        dichotomy(-1,1,10e-5);
    }
}
class Function{
    public static double setF(double x){
        return Math.sin(x);
    }
}
