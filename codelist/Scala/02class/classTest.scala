import java.io.{File, PrintWriter} 
import scala.io.Source
import scala.collection.mutable.Map

object HelloWorld {
    def main(args: Array[String]): Unit = {
        val cs = new CheckAccSum()
        cs.add(1)
        println(cs.checkSum())
        println(CheckAccSum.calculate("Hello World"))
        println(CheckAccSum.calculate("Hello xiaolong"))
        println(CheckAccSum.calculate("Hello xiaolong"))
    }
}
/*
 *Scala的缺省修饰符为public ，也就是如果不带有访问范围的修饰符public,protected,private，Scala缺省定义为 public。
 * 类的方法以def定义开始，要注意的Scala的方法的参数都是val类型，而不是var类型，因此在函数体内不可以修改参数的值
 */
class CheckAccSum{
  private var sum = 0
  def add(b:Byte):Unit = sum+=b
  def checkSum():Int = ~ (sum & 0xFF) + 1
}

/*
 * 伴生对象
 */
object CheckAccSum{
  private val cache = Map[String,Int]()
  def calculate(s:String):Int = {
    if(cache.contains(s)){
      cache(s)
    }
    else{
      val cs = new CheckAccSum()
      for( c <- s){
          cs.add(c.toByte)
      }
      val su = cs.checkSum()
      cache += (s -> su)
      su
    }
  }
  
}