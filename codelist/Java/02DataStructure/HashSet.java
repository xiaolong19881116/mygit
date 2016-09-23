import java.util.HashMap;  
import java.util.HashSet;  
import java.util.Iterator;  
import java.util.Set;  
  
public class Test {  
  
    public static void main(String[] args) {  
    	HashSet hs = new HashSet();
    	hs.add(1);
    	hs.add(1);
    	hs.add(2);
    	hs.add(3);
    	hs.add("hello");
    	System.out.println(hs);
    	Iterator it = hs.iterator();
    	while(it.hasNext()){
    		Object obj = it.next();
    		if(obj instanceof Integer){
    		    System.out.println("integer:"+obj);
    		   }
    	}
    	
    	System.out.println(hs.contains(3));
    	hs.remove(3);
    	System.out.println(hs.contains(3));
    	System.out.println(hs);
    }  
}  