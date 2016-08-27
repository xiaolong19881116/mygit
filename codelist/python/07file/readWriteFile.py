#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for file"
 
__author__ = 'mxl'

readf = open("input.txt","r")
lines = readf.readlines()
for line in [i.strip() for i in lines]:
    print line
readf.close()

with open("output.txt","w") as wf:
    wf.writelines(lines)