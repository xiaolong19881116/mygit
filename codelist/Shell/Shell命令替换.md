# 命令替换

命令替换是指Shell可以先执行命令，将输出结果暂时保存，在适当的地方输出。

命令替换的语法：

    `command`

注意是反引号，不是单引号，这个键位于 Esc 键下方。

下面的例子中，将命令执行结果保存在变量中：

    #!/bin/bash
    DATE=`date`
    echo "Date is $DATE"
    USERS=`who | wc -l`
    echo "Logged in user are $USERS"
    UP=`date ; uptime`
    echo "Uptime is $UP"

运行结果：

    Date is Thu Jul  2 03:59:57 MST 2009
    Logged in user are 1
    Uptime is Thu Jul  2 03:59:57 MST 2009
    03:59:57 up 20 days, 14:03,  1 user,  load avg: 0.13, 0.07, 0.15

#命令替换是的shell与其他语言结合起来

    gcc -o simpleC simpleC.c
    testc = `./simpleC`
    echo $testc
    echo $?