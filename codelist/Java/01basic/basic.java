import java.text.DecimalFormat; //��ʽ��double
import java.util.Scanner;//��׼����

public class Test {
    public static void main(String args[]){
    	 Integer x = 30;
	     double y = 1.23;
	     String z = "Hello World!";
	     int[] li = {1,2,3};
	     System.out.println(x);
	     
	     System.out.println(Integer.toHexString(x)  );//ת16����
	     System.out.println(Integer.toOctalString(x)  );//ת8����
	     System.out.println(Integer.toBinaryString(x)  );//ת2����
	     
	     System.out.println(x.getClass());
	     System.out.println(x.getClass().getName());
	     System.out.println(x.getClass().getName()=="java.lang.Integer"); //��ȡ�������� 
	     System.out.println(y);
	     //System.out.println(y);
	     DecimalFormat df1 = new DecimalFormat("####.000"); //����3λС��
	     System.out.println(df1.format(1234.56));
	     System.out.println(df1.format(y));
	     
	     System.out.println(z);
	     System.out.println(li[0]);
	     System.out.println(li.hashCode());//Java�������ȡ�����ڴ��ַ������ʹ�� == ����hashCode()
	         
	     Scanner sc = new Scanner(System.in); 
	     System.out.println("������һ���ַ���");
	     String text = sc.nextLine();
	     System.out.println("��������ַ�����:" + text);
	     
    }
}
