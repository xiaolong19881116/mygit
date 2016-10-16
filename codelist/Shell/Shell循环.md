for循环一般格式为：

    for 变量 in 列表
    do
    command1
    command2
    ...
    commandN
    done

eg:

    for loop in 1 2 3 4 5
    do
    echo "The value is: $loop"
    done

显示主目录下以 .bash 开头的文件：

    #!/bin/bash
    for FILE in $HOME/.bash*
    do
       echo $FILE
    done

while循环用于不断执行一系列命令，也用于从输入文件中读取数据；命令通常为测试条件。其格式为：

    while command
    do
       Statement(s) to be executed if command is true
    done
命令执行完毕，控制返回循环顶部，从头开始直至测试条件为假。

以下是一个基本的while循环，测试条件是：如果COUNTER小于5，那么返回 true。COUNTER从0开始，每次循环处理时，COUNTER加1。运行上述脚本，返回数字1到5，然后终止。
    
    COUNTER=0
    while [ $COUNTER -lt 5 ]
    do
    COUNTER='expr $COUNTER + 1'
    echo $COUNTER
    done
    
    运行脚本，输出：
    1
    2
    3
    4
    5

while循环可用于读取键盘信息。下面的例子中，输入信息被设置为变量FILM，按<Ctrl-D>结束循环。

    echo 'type <CTRL-D> to terminate'
    echo -n 'enter your most liked film: '
    while read FILM
    do
    echo "Yeah! great film the $FILM"
    done
    
    运行脚本，输出类似下面：
    
    type <CTRL-D> to terminate
    enter your most liked film: Sound of Music
    Yeah! great film the Sound of Music

guess number

    echo "please input the number(1-10)"
    read num 
    
    while(( 1 >= 0 ))
    do 
      if [ "$num" -eq 4 ]
      then 
      echo "Congratulations! You are right"
      exit 0
      elif [ "$num" -lt 4 ]
      then
      echo "Too small try again:"
      read num 
      elif [ "$num" -gt 4 ]
      then 
      echo "Too big try again:"
      read num
      else 
      exit 0
      fi
    done

break & case

    #!/bin/bash
    while :
    do
    echo -n "Input a number between 1 to 5: "
    read aNum
    case $aNum in
    1|2|3|4|5) echo "Your number is $aNum!"
    ;;
    *) echo "You do not select a number between 1 to 5, game is over!"
    break
    ;;
    esac
    done