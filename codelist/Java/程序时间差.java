
public class Test {
    public static void main(String args[]){
    	   	
    	int[] array = new int[10];
        System.out.println("array�ĸ����ǣ�" +  array.getClass().getSuperclass());
        System.out.println("array�������ǣ�" + array.getClass().getName());	   
        
        int[] a = new int[2]; 
        int[] b = new int[] {1,2,3};
        int[] c = {1,2,3};
        System.out.println(a[0]);
        System.out.println(b[0]);
        System.out.println(c[0]);
        
        Long time1 = System.currentTimeMillis();
        int sum = 0;
        for (int i=1;i<100000000;i++) {sum = sum + i;}
        Long time2 = System.currentTimeMillis();
        
        System.out.println("������ʱ�䣺" + (time2 - time1) + "����");
        
    }
}
