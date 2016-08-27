#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for reducer"
 
__author__ = 'mxl'

import os

def Reduce(SourceFolder,targetFile):
    if not os.path.isdir(SourceFolder):
        print SourceFolder,"is not exist!"
        return
    result = {}
    files = [SourceFolder+'\\'+f for f in os.listdir(SourceFolder) if f.endswith("_map.txt")]
    for f in files:
        with open(f,"r") as rf:
            for line in rf:
                line = line.strip()
                if not line:
                    continue
                p = line.index(":")
                key = line[0:p]
                value = int(line[p+1:])
                result[key] = result.get(key,0) + value
    with open(targetFile,"w") as wf:
        for k,v in result.items():
            wf.write(k+":"+str(v)+"\n")

if __name__ == "__main__":
    Reduce("output_split","output_split\\result.txt")
