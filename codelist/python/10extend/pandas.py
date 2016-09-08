#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for pandas"

import pandas as pd 
from pandas import Series , DataFrame 

sli = [100,"hello","xianlong"]
s = Series(sli)
print s
print s.values
print s.index

dict1 = {"C":100,"C++":200,"C#":300,"python":150}
s2 = Series(dict1)
print s2

print "---------------------------------------------"

dict2 = {"C":[100,200],"C++":[200,300],"C#":[300,400],"python":[150,350]}
df = DataFrame(dict2)
print df
df.index = ["begin","end"]  #修改行名
df.columns = ["A","B","C","D"] #修改列名
print df.columns 
print df
print df.values
print df["A"]["end"]

print "---------------------------------------------"

"读取 csv 文件"
marks = pd.read_csv("abc.csv") #as DataFrame
print marks

print "---------------------------------------------"

"读取 .xls 或者 .xlsx 文件"
xls = pd.ExcelFile("abc.xlsx") #as DataFrame
print xls.sheet_names
sheet1 = xls.parse("Sheet1")
print sheet1 