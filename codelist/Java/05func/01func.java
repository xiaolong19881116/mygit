import java.util.Arrays;
import java.util.List;
import java.util.Comparator;
import java.util.Collections;
public class Test {  

    public static void main(String args[])  
    {
    	println("Hello World!");
    	double re = returnMax(1,2,3);
    	println(re+1);
    	String[] sour = {"Rafael Nadal", "Novak Djokovic",  
    		       "Stanislas Wawrinka",  
    		       "David Ferrer","Roger Federer",  
    		       "Andy Murray","Tomas Berdych",  
    		       "Juan Martin Del Potro"};
    	for(String x : sour){
    		println(x);
    	}
    	List<String> players = Arrays.asList(sour);
    	//players.forEach((player) -> System.out.print(player + "; "));  
    	println(players);
    	//Arrays.sort(players, (String s1, String s2) -> (s1.compareTo(s2))); //lambda jdk 8
    	// 1.1 使用匿名内部类根据 name 排序 players  
    	Comparator<String> sortByName = new Comparator<String>(){
    		public int compare(String s1, String s2) {  
    	        return (s1.compareTo(s2));
    		}
    	};
    	//Arrays.sort(players,sortByName);
    	Collections.sort(players,sortByName);
    	println(players);
    }  
    
    public static void println(Object s){
    	System.out.println(s.toString());
    }
    
    public static double returnMax(double... nums){ 
    	if(nums.length == 0){
    		println("error");
    	}
    	
    	double re = nums[0];
    	for(double x:nums){
    		if(x > re){
    			re = x;
    		}
    	}
    	println("result max is :"+re);
    	return re;
    }
}  