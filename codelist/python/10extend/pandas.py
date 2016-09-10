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
# https://picklecai.gitbooks.io/omoocdata/content/note/classnote/ch4pandas.html 
# df_pop = pd.read_csv("european_cities.csv", delimiter=",", encoding="utf-8", header=0)
# df_pop.info() # 观察元信息
# df_pop["NumericPopulation"] = df_pop.Population.apply(lambda x:int(x.replace(",",""))) 
# df_pop["State"].values[:3] 
# df.head() #取前几行信息
# df.ix[['Paris','Rome']] 读取多行
# df_pop["State"] = df_pop.State.apply(lambda x: x.strip()) 

# df_pop2 = df_pop.set_index("City")
# df_pop2 = df_pop2.sort_index()
# df_pop3 = df_pop.set_index(["State","City"]) 
# df_pop3 = df_pop.set_index(["State","City"]).sortlevel(0) 
# df_pop3.ix["Sweden"]

# df_pop.set_index("City").sort(["State", "NumericPopulation"], ascending=[False, True]).head() 

# df_pop3 = df_pop[["State", "City", "NumericPopulation"]].set_index(["State", "City"])


##fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,4))
##
##city_counts.plot(kind="barh", ax=ax1)
##ax1.set_xlabel("# cities in top 105")
##
##df_pop5.NumericPopulation.plot(kind="barh", ax=ax2)
##ax2.set_xlabel("Total pop in top 105 cities")
##
##fig.tight_layout()
##fig.savefig("ch4-state-city-counts-sum.pdf")
##
##marks = pd.read_csv("abc.csv") #as DataFrame
print marks

print "---------------------------------------------"

"读取 .xls 或者 .xlsx 文件"
xls = pd.ExcelFile("abc.xlsx") #as DataFrame
print xls.sheet_names
sheet1 = xls.parse("Sheet1")
print sheet1 