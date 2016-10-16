函数可以让我们将一个复杂功能划分成若干模块，让程序结构更加清晰，代码重复利用率更高。像其他编程语言一样，Shell 也支持函数。Shell 函数必须先定义后使用。

Shell 函数的定义格式如下：

    function_name () {
    list of commands
    [ return value ]
    }
如果你愿意，也可以在函数名前加上关键字 function：

    function function_name () {
    list of commands
    [ return value ]
    }
函数返回值，可以显式增加return语句；如果不加，会将最后一条命令运行结果作为返回值。

Shell 函数返回值只能是整数，一般用来表示函数执行成功与否，0表示成功，其他值表示失败。如果 return 其他数据，比如一个字符串，往往会得到错误提示：“numeric argument required”。

如果一定要让函数返回字符串，那么可以先定义一个变量，用来接收函数的计算结果，脚本在需要的时候访问这个变量来获得函数返回值。

    #!/bin/bash
    # Define your function here
    Hello () {
       echo "Url is http://see.xidian.edu.cn/cpp/shell/"
    }
    # Invoke your function
    Hello

运行结果：

    $./test.sh
    Hello World
    $
调用函数只需要给出函数名，不需要加括号。

再来看一个带有return语句的函数：

    #!/bin/bash
    funWithReturn(){
    echo "The function is to get the sum of two numbers..."
    echo -n "Input first number: "
    read aNum
    echo -n "Input another number: "
    read anotherNum
    echo "The two numbers are $aNum and $anotherNum !"
    return $(($aNum+$anotherNum))
    }
    funWithReturn
    # Capture value returnd by last command
    ret=$?
    echo "The sum of two numbers is $ret !"

运行结果：
    
    The function is to get the sum of two numbers...
    Input first number: 25
    Input another number: 50
    The two numbers are 25 and 50 !
    The sum of two numbers is 75 !
    #函数返回值在调用该函数后通过 $? 来获得。

再来看一个函数嵌套的例子：

    #!/bin/bash
    # Calling one function from another
    number_one () {
       echo "Url_1 is http://see.xidian.edu.cn/cpp/shell/"
       number_two
    }
    number_two () {
       echo "Url_2 is http://see.xidian.edu.cn/cpp/u/xitong/"
    }
    number_one
    运行结果：
    Url_1 is http://see.xidian.edu.cn/cpp/shell/
    Url_2 is http://see.xidian.edu.cn/cpp/u/xitong/


#特殊变量	说明

- $#	传递给函数的参数个数。
- $*	显示所有传递给函数的参数。
- $@	与$*相同，但是略有区别，请查看Shell特殊变量。
- $?	函数的返回值。

在Shell中，调用函数时可以向其传递参数。在函数体内部，通过 $n 的形式来获取参数的值，例如，$1表示第一个参数，$2表示第二个参数...

#带参数的函数示例：

    #!/bin/bash
    funWithParam(){
    echo "The value of the first parameter is $1 !"
    echo "The value of the second parameter is $2 !"
    echo "The value of the tenth parameter is $10 !"
    echo "The value of the tenth parameter is ${10} !"
    echo "The value of the eleventh parameter is ${11} !"
    echo "The amount of the parameters is $# !"  # 参数个数
    echo "The string of the parameters is $* !"  # 传递给函数的所有参数
    }
    funWithParam 1 2 3 4 5 6 7 8 9 34 73

运行脚本：

    The value of the first parameter is 1 !
    The value of the second parameter is 2 !
    The value of the tenth parameter is 10 !
    The value of the tenth parameter is 34 !
    The value of the eleventh parameter is 73 !
    The amount of the parameters is 12 !
    The string of the parameters is 1 2 3 4 5 6 7 8 9 34 73 !"
    #注意，$10 不能获取第十个参数，获取第十个参数需要${10}。当n>=10时，需要使用${n}来获取参数。