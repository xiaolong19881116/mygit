# 异常 #
Scala中的异常可以在try-catch-finally语法中通过模式匹配使用。
    
    try {
      remoteCalculatorService.add(1, 2)
    } catch {
      case e: ServerIsDownException => log.error(e, "the remote calculator service is unavailable. should have kept your trusty HP.")
    } finally {
      remoteCalculatorService.close()
    }

try也是面向表达式的

    val result: Int = try {
      remoteCalculatorService.add(1, 2)
    } catch {
      case e: ServerIsDownException => {
    log.error(e, "the remote calculator service is unavailable. should have kept your trusty HP.")
    0
      }
    } finally {
      remoteCalculatorService.close()
    }
    
这并不是一个完美编程风格的展示，而只是一个例子，用来说明try-catch-finally和Scala中其他大部分事物一样是表达式。

当一个异常被捕获处理了，finally块将被调用；它不是表达式的一部分。