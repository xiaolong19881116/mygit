#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for FileSplit"
 
__author__ = 'mxl'

import os
import os.path

def FileSplit(sourceFile,targetFolder):
    if not os.path.isfile(sourceFile):
        print sourceFile,"is not exist!"
        return
    if not os.path.isdir(targetFolder):
        os.mkdir(targetFolder)
    fileNum = 1
    number = 100
    tempData = []
    f = open(sourceFile,"r")
    line = f.readline()
    while line:
        for i in range(number):
            tempData.append(line)
            line = f.readline()
            if not line:
                break
        destFile = os.path.join(targetFolder,sourceFile[0:-5]+str(fileNum)+".txt")
        with open(destFile,"w") as wf:
            wf.writelines(tempData)
        tempData = []
        fileNum = fileNum + 1
    f.close()

if __name__ == "__main__":
    sourceFile = "output.html"
    targetFolder = sourceFile[0:-5] + "_split"
    FileSplit(sourceFile,targetFolder)