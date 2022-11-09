public class demo {
    int n;
    int []arr;
    public void setN(int n){
        this.n=n;
    }
    public void Fibonacci(){
        arr=new int[n];
        if(n==1&&n==2){
            for(int i=0;i<n;i++ )
                arr[i]=1;
        }
        else{int x=1,y=1,temp=x;
            for (int i=1;i<=n;i++){
                arr[i-1]=temp;
               x=y;
               y=temp+y;
               temp=x;
            }
        }
    }
    public void show(){
        for(int i=0;i<arr.length;i++){
            System.out.println("F["+i+"]="+arr[i]);
        }
    }

}
