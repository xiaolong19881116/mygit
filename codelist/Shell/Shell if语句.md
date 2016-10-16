if 语句通过关系运算符判断表达式的真假来决定执行哪个分支。Shell 有三种 if ... else 语句：

- if ... fi 语句；
- if ... else ... fi 语句；
- if ... elif ... else ... fi 语句。

最后必须以 fi 来结尾闭合 if，fi 就是 if 倒过来拼写，后面也会遇见。

***注意：expression 和方括号([ ])之间必须有空格，否则会有语法错误。***

eg

    #!/bin/sh
    a=10
    b=20
    if [ $a == $b ]
    then
       echo "a is equal to b"
    elif [ $a -gt $b ]
    then
       echo "a is greater than b"
    elif [ $a -lt $b ]
    then
       echo "a is less than b"
    else
       echo "None of the condition met"
    fi