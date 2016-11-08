import java.io.{File, PrintWriter} 
import scala.io.Source
import scala.collection.mutable.Map

object HelloWorld {
    def main(args: Array[String]): Unit = {
        val r = new Rational(5,7)
        val s = new Rational(2,7)
        val ss = new Rational(2)
        val f = new Rational(33,77)
        println(r+s)
        println(r*s)
        println(r+2)
        println(f)
        println(f.format())
        println(r.max(s))
        println(ss)
        println(r.add(s))
        println(r)
        println(r.getClass())
        println(r.getClass().getName())
        println(r.getClass().getName() == "Rational")
    }
}
class Rational(n:Int,d:Int){
  //require方法为Predef对象的定义的一个方法，Scala环境自动载入这个类的定义，因此无需使用import引入这个对象
  require(d!=0) //分母不能为0
  val num = n
  val den = d
  private val g =gcd (n.abs,d.abs)
  override def toString = num + "/" + den
  def add(that:Rational) = new Rational(den*that.num + num*that.den,den*that.den)
  def lessThan(that:Rational) = this.num * that.den < that.num * this.den
  def max(that:Rational) = if(lessThan(that)) that else this
  def this(n:Int) = this(n,1) //辅助构造函数
  private def gcd(a:Int,b:Int):Int =  if(b==0) a else gcd(b, a % b)
  def format():Rational = new Rational(this.num/g,this.den/g)
  def +(that:Rational)  = new Rational(den*that.num + num*that.den,den*that.den) //运算符重载
  def + (i:Int) = new Rational (num + i * den, den)//Rational + 整数
  def *(that:Rational)  = new Rational( num * that.num, den * that.den)
  implicit def intToRational(x:Int) = new Rational(x) //定义隐式转换 解决 整数+Rational 
 }