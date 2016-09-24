/**
* The HelloWorld program implements an application that
* simply displays "Hello World!" to the standard output.
*
* @author  xianlong.mxl
* @version 1.0
* @since   2016-09-24 
*/
public class Test {  

    public static void main(String args[])  
    {
    	HelloWorld c = new HelloWorld();
    	c.Hello();
    	System.out.println(addNum(20,30));
    }  
    
    /**
     * This method is used to add two integers. This is
     * a the simplest form of a class method, just to
     * show the usage of various javadoc Tags.
     * @author  xianlong.mxl
     * @param numA This is the first paramter to addNum method
     * @param numB  This is the second parameter to addNum method
     * @return int This returns sum of numA and numB.
     */
     public static int addNum(int numA, int numB) {
        return numA + numB;
     }
}  