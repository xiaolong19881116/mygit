#!/bin/bash

echo "Hello World!"

echo "processID is $$" #���̺�

echo "father ProcessID is $PPID" #�����̺�


echo -e -n "\033[47m  " #��ʾ�׸�

echo -e -n "\033[40m  " #��ʾ�ڸ�

echo -e -n "\033[47m  " #��ʾ�׸�


echo -e -n "\033[40m  " #��ʾ�ڸ�

your_name="mozhiyan"
echo $your_name
echo ${your_name}

#�Ƽ������б������ϻ����ţ����Ǹ��õı��ϰ�ߡ�
for skill in Ada Coffe Action Java 
do
    echo "I am good at ${skill}Script"
done