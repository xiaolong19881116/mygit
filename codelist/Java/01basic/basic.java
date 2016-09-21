import java.text.DecimalFormat; //格式化double
import java.util.Scanner;//标准输入

public class Test {
    public static void main(String args[]){
    	 Integer x = 30;
	     double y = 1.23;
	     String z = "Hello World!";
	     int[] li = {1,2,3};
	     System.out.println(x);
	     
	     System.out.println(Integer.toHexString(x)  );//转16进制
	     System.out.println(Integer.toOctalString(x)  );//转8进制
	     System.out.println(Integer.toBinaryString(x)  );//转2进制
	     
	     System.out.println(x.getClass());
	     System.out.println(x.getClass().getName());
	     System.out.println(x.getClass().getName()=="java.lang.Integer"); //获取对象类型 
	     System.out.println(y);
	     //System.out.println(y);
	     DecimalFormat df1 = new DecimalFormat("####.000"); //保留3位小数
	     System.out.println(df1.format(1234.56));
	     System.out.println(df1.format(y));
	     
	     System.out.println(z);
	     System.out.println(li[0]);
	     System.out.println(li.hashCode());//Java不建议获取对象内存地址，可以使用 == 或者hashCode()
	         
	     Scanner sc = new Scanner(System.in); 
	     System.out.println("请输入一串字符串");
	     String text = sc.nextLine();
	     System.out.println("您输入的字符串是:" + text);
	     
    }
}
