//import java.io.{File, PrintWriter} 
//import scala.io.Source
//import scala.collection.mutable.Map

object HelloWorld {
    def main(args: Array[String]): Unit = {
        /*
         * Scala中函数为头等公民，你不仅可以定义一个函数然后调用它，而且你可以写一个未命名的函数字面量，然后可以把它当成一个值传递到其它函数或是赋值给其它变量。
         * 下面的例子为一个简单的函数字面量（参考整数字面量，3 为一整数字面量）
         * var increase = (x :Int ) => x +1
         * (x :Int ) => x +1 函数字面量 符好 => 表示这个函数将符号左边的东西（本例为一个整数），转换成符号右边的东西（加1）
         * 简化 -1 ：去掉类型 (x) => x +1
         * 简化 -2 ：去掉括号x => x +1
         * Scala允许使用”占位符”下划线”_”来替代一个或多个参数：
         */
      val someNumbers = List ( -11, -10, - 5, 0, 5, 10)
      val fliNum = someNumbers.filter(_ >0)
      fliNum.foreach(println(_))
      val arr= Array("What's","up","doc?")
      echo(arr:_*) //调用数组
      echo("hello")
      echo("ac","cs")
      /*
       * Scala在定义函数时允许指定最后一个参数可以重复（变长参数）
       */
      def echo(myArgs:String *) = for (myArg <- myArgs) println(myArg)
             
    }
}
 