import java.util.ArrayList;  
import java.util.Arrays; 
import java.util.List; 
import java.util.Collections;

public class Test {
    public static void main(String args[]){
    	   	
        
        int[] a = new int[2]; 
        int[] b = new int[] {1,2,3};
        int[] c = {1,2,3};
        System.out.println(a[0]);
        System.out.println(b[0]);
        System.out.println(c[0]);
        
        ArrayList al = new ArrayList();
        al.add(10);
        al.add(20);
        al.add(30);
        al.add(1.23);
        al.add("1.23");
        System.out.println(al);
        System.out.println(al.get(0));
        System.out.println(al.get(3));
        System.out.println(al.get(4));

                
        ArrayList<Integer> Ilist = new ArrayList<Integer>();
        Ilist.add(100);
        Ilist.add(200);
        Ilist.add(300);
        Ilist.add(200);
        System.out.println(Ilist.size());
        
        for (int x : Ilist){
        	System.out.println(x);
        }
        System.out.println(Ilist.indexOf(300));
        System.out.println(Ilist.lastIndexOf(300));
        System.out.println(Ilist.indexOf(500));
        
        System.out.println(Collections.max(Ilist));
        System.out.println(Collections.min(Ilist));
        
        Collections.sort(Ilist);
        for (int x : Ilist){
        	System.out.println(x);
        }
        //System.out.println(Ilist.get(2));//200
    }
}
