Shell编程

'''
#!bin/bash
date #显示日期

who #显示登录用户
'''

保存为whologged.sh

ls -l whologged.sh #查看文件权限 有没有执行权限即X权限

chmod u+x whologged.sh #添加X执行权限

sh ./whologged.sh #执行Shell脚本