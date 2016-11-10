//import java.io.{File, PrintWriter} 
//import scala.io.Source
//import scala.collection.mutable.Map

object HelloWorld {
    def main(args: Array[String]): Unit = {
      FooMaker() 
      println(AddOne(1))
      val add2 = new AddTwo()
      println(add2(2))
      println(AddThree(3))
    }
}

class Foo{
  println("foo create")
}

object FooMaker{
  def apply() = new Foo()
}
/*
 * 函数是一些特质的集合。具体来说，具有一个参数的函数是Function1特质的一个实例。这个特征定义了apply()语法糖，让你调用一个对象时就像你在调用一个函数
 */
object AddOne extends Function1[Int,Int]{
  def apply(m:Int) = m + 1
}
/*
 * class也可以
 */
class AddTwo extends Function1[Int,Int]{
  def apply(m:Int) = m + 2
}
/*
 * 使用更直观快捷的extends (Int => Int)代替extends Function1[Int, Int]
 */
object AddThree extends (Int => Int){
  def apply(m:Int) = m + 3
}
