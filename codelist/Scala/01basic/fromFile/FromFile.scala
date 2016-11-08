import scala.io.Source

object FromFile {
    def main(args:Array[String]):Unit ={
        if(args.length>0){
            for(line<- Source.fromFile(args(0)).getLines){
                println(line.length + " | " + line)
            }
        }
        else {
            println("please input file")
        }
    }
}