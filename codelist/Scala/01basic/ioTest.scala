import java.io.{File, PrintWriter} 
import scala.io.Source
object HelloWorld {
    def main(args: Array[String]): Unit = {
        println("Hello, world!")
        // val & var
        var var1 = 1  //可变
        var1 += 1
        println(var1)
        val val1 = 1 //不可变
       // val1 += 1
        println(val1)
        
        /*********************标准输入输出**********************/
        //readInt、readDouble、readByte、readShort、readLong、readFloat、readBoolean或者readChar
        val name = readLine("Your name:")
        print("Your age:")
        val age = readInt()
        val age2:Int = readLine("Your age2:").toInt
        println(age2+10)
        printf("Hello, %s! Next year, your will be %d.\n", name, age + 1)
        
        /*********************文件读取与写入**********************/
        val fileNmae = "output.txt"
        val wt = new PrintWriter(new File(fileNmae))
        wt.write("Hello World\n")
        wt.write("Hello xiaolong\n")
        wt.close()
        
        for(line<- Source.fromFile(fileNmae).getLines){
            println(line.length + " | " + line)
          }
    }
}