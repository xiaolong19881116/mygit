#!/bin/bash

echo "Hello World!"

echo "processID is $$" #进程号

echo "father ProcessID is $PPID" #父进程号


echo -e -n "\033[47m  " #显示白格

echo -e -n "\033[40m  " #显示黑格

echo -e -n "\033[47m  " #显示白格


echo -e -n "\033[40m  " #显示黑格

your_name="mozhiyan"
echo $your_name
echo ${your_name}

#推荐给所有变量加上花括号，这是个好的编程习惯。
for skill in Ada Coffe Action Java 
do
    echo "I am good at ${skill}Script"
done