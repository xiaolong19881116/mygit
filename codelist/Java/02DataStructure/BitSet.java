import java.util.BitSet;  

public class Test {  

    public static void main(String args[])  
    {  
       BitSet bs = new BitSet(10);//size = 10
       System.out.println(bs.toString());
       bs.set(3);
       bs.set(5);
       bs.set(8);
       System.out.println(bs.toString());
       System.out.println(bs.get(0));
       System.out.println(bs.get(1));
       System.out.println(bs.get(3));
       
       int[] shu={2,42,5,6,6,18,33,15,25,31,28,37};
       BitSet bm1=new BitSet(50); 
       for(int i = 0;i<shu.length;i++){
    	   bm1.set(shu[i]);
       }
       System.out.println(bm1.toString());
       
    }  
}  