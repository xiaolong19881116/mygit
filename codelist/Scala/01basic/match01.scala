//import java.io.{File, PrintWriter} 
//import scala.io.Source
//import scala.collection.mutable.Map

/*
 * 模式匹配
 */
object HelloWorld {
    def main(args: Array[String]): Unit = {
        /*
         * 值匹配
         */
      val x = 3
      val y = x match {
        case 1 => "one"
        case 2 => "two"
        case _ => "many"
      }
      printf("%d is %s\n",x,y)
      /*
       * 添加条件匹配
       */
      
      val z =  x match {
        case i if i == 1 => "one"
        case i if i == 2 => "two"
        case _ => "many"
      }
      printf("%d is %s\n",x,z)
      
      /*
       * 匹配类型
       */
      def bigger(o:Any):Any ={
          o match {
            case d:Int => d + 1
            case d:Double => d + 0.1
            case d:String => d + "s"
            case _ => "others"
          }
      }
      println(bigger(1))
      println(bigger(1.0))
      println(bigger("cat"))
      
      val hp20b = Calculator("hp", "20B")
      val hp20B = Calculator("hp", "20B")
      println(hp20b == hp20B)
      
      def calcType(calc: Calculator) = calc match {
          case Calculator("hp", "20B") => "financial"
          case Calculator("hp", "48G") => "scientific"
          case Calculator("hp", "30B") => "business"
          case _ => "Calculator of unknown type"
      }
      
      println(calcType(hp20b))
    }
}
/*
 * 样本类 Case Classes
 *使用样本类可以方便得存储和匹配类的内容。你不用new关键字就可以创建它们。
 */
case class Calculator(brand: String, model: String)
