#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for mapper"
 
__author__ = 'mxl'

import os
import re 
import os.path
import threading

def Map(sorceFile):
    if not os.path.isfile(sorceFile):
        print sorceFile,"is not exist"
        return
    pattern = re.compile("[a-zA-Z0-9]")
    result = {} 
    with open(sorceFile,"r") as f:
        for line in f:
            r = pattern.findall(line)
            for x in r:
                t = result.get(x,0)
                t = t + 1
                result[x] = t
    destFile = sorceFile[0:-4] + '_map.txt'
    with open(destFile,"w") as wf:
        for k,v in result.items():
            wf.write(k + ":" +str(v) + '\n')

if __name__ == "__main__":
    destFolder = "output_split"
    files = os.listdir(destFolder)
    print files

    def Main(i):
        Map(os.path.join(destFolder,files[i]))
    #使用多线程
    for i in range(len(files)):
        t = threading.Thread(target = Main,args = (i,))
        t.start()