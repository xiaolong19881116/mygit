//import java.io.{File, PrintWriter} 
//import scala.io.Source
//import scala.collection.mutable.Map

object HelloWorld {
    def main(args: Array[String]): Unit = {
        for (arg <- args){
          print(arg+" ")
        }
        println(args.length)
        println(args(0))//第一个参数，非文件名
        
        val ret = args(0) match{
          case "xl" => "xiaolong"
          case "yy" => "yyyy"
          case _ => "other"
        }
        println(ret)
    }
}
 