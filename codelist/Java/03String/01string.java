
public class Test {  

    public static void main(String args[])  
    {  
       String site = "www.taobao.com";
       System.out.println(site.toUpperCase());//toUpperCase
       System.out.println(site);
       System.out.println("   abc  ".trim());//trim
       System.out.println(site.startsWith("www"));//startsWith
       System.out.println(site.endsWith("com"));//endsWith
       System.out.println(site.length());
       System.out.println(site.concat("/index"));//concat
       System.out.println(site);
       System.out.println(site.replace("w", "*"));//replace
       System.out.println(site);
       System.out.println(site.substring(4,10));//substring
       System.out.println(site);
       
       
       
       String[] sli = site.split("\\.");// split regex 
       for(String x:sli){
    	   System.out.println(x);
       }
       System.out.println(site);
       
       double floatVar = 1.234;
       int intVar =123 ;
       System.out.printf("�����ͱ����ĵ�ֵΪ " +
               "%10.2f, ���ͱ�����ֵΪ " +
               " %d, �ַ���������ֵΪ " +
               "is %s\n", floatVar, intVar, site);
       String fs;
       fs = String.format("�����ͱ����ĵ�ֵΪ " +
                          "%f, ���ͱ�����ֵΪ " +
                          " %d, �ַ���������ֵΪ " +
                          " %s\n", floatVar, intVar, site);
       System.out.println(fs);
       
    }  
}  