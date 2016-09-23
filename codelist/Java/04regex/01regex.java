//regex
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Test {  

    public static void main(String args[])  
    {  
    	String regEx = "<a>([\\d]*?)</a>";
        String s = "<a>123</a><a>456</a><a>789</a>";
        Pattern pat = Pattern.compile(regEx);
        Matcher mat = pat.matcher(s);
        boolean rs = mat.find();
        for(int i=1;i<=mat.groupCount();i++){
            System.out.println(mat.group(i));
        }
    	
       String line = "This order 11 was 22 placed for QT 3000 ! OK?";
       //String pattern = "(.*)(\\d+)(.*)";
       String pattern = "(\\d+)"; //ok 
       String pattern2 = "\\s"; //ok 
       Pattern r = Pattern.compile(pattern);
       Pattern r2 = Pattern.compile(pattern2);
       Matcher m = r.matcher(line);
    
       if (m.find()) {
    	   String digitNumList = m.group();
    	   System.out.println(digitNumList );
    	   System.out.println("Found value: " + m.group() );
           System.out.println("Found value: " + m.group(0) );
           System.out.println("Found value: " + m.group(1) );
           //System.out.println("Found value: " + m.group(2) );
        } else {
           System.out.println("NO MATCH");
        }
       
       String output = m.replaceAll("#");
       System.out.println(output);
       
       System.out.println(line);
       String[] tokens = r2.split(line);
       for(String x:tokens){
    	   System.out.println(x);
       }
       
       
       
    }  
}  