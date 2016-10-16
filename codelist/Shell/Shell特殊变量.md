- $0	当前脚本的文件名
- $n	传递给脚本或函数的参数。n 是一个数字，表示第几个参数。例如，第一个参数是$1，第二个参数是$2。
- $#	传递给脚本或函数的参数个数。
- $*	传递给脚本或函数的所有参数。
- $@	传递给脚本或函数的所有参数。被双引号(" ")包含时，与 $* 稍有不同，下面将会讲到。
- $?	上个命令的退出状态，或函数的返回值。
- $$	当前Shell进程ID。对于 Shell 脚本，就是这些脚本所在的进程ID。

    #!/bin/bash
    echo "File Name: $0"
    echo "First Parameter : $1"
    echo "First Parameter : $2"
    echo "Quoted Values: $@"
    echo "Quoted Values: $*"
    echo "Total Number of Parameters : $#"

运行结果：
    $./test.sh Zara Ali
    File Name : ./test.sh
    First Parameter : Zara
    Second Parameter : Ali
    Quoted Values: Zara Ali
    Quoted Values: Zara Ali
    Total Number of Parameters : 2