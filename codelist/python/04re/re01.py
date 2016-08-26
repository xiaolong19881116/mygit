#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for re"
 
__author__ = 'mxl'

#常用的正则元字符
'''
. 匹配除了换行以外的任意单个字符
* 匹配位于*前的0个或多个字符
+ 匹配位于+前的1个或多个字符
? 匹配位于？前的1个或0个字符
| 或运算
^ 匹配行首
$ 匹配行尾
[] 匹配位于[]内任意一个字符标示范围
() 将位于()内的内容当成一个整体对待
{} {m,n}匹配重复次数m,n之间
\b 单词头或者单词尾; \B含义相反
\d 匹配数字,[0-9];  \D含义相反
\s 匹配任意空白符;   \S含义相反
\w 匹配字母、数字、下划线 [a-zA-Z0-9_]; \W含义相反
'''

import re
  
#分割成列表
text = "xiaolong.xiao...yaya jyy"
patStr = '[\. ]+' #注有一个空格
print re.split(patStr,text) #使用re模块的方法
pattern = re.compile(patStr) #编译成对象提高字符串处理速度
print pattern.split(text)

#查找全部
patStr2 = '[a-zA-Z]+'
print re.findall(patStr2,text)
pattern2 = re.compile(patStr2)
print pattern2.findall(text)

#替换模式匹配字符串
patStr3 = '[xy]'
print re.sub(patStr3,'*',text)
pattern3 = re.compile(patStr3)
print pattern3.sub('@',text)

#模式匹配match match从字符串开头匹配，开头匹配不成功返回None
patStr4 = 'xiao|long'
print re.match(patStr4,'xiao')
print re.match(patStr4,'xiao').group()

pattern4 = re.compile(patStr4)
print pattern4.match('long')
print pattern4.match('long').group()

print pattern4.match('lng')
#print pattern4.match('lng').group()

#模式匹配search 匹配整个字符串直到找到匹配
patStr5 = '(ya){1,}'
print re.search(patStr5,text)
print re.search(patStr5,text).group()
print re.search(patStr5,text).group(0)
print re.search(patStr5,text).group(1)

pattern5 = re.compile(patStr5)
print pattern5.search(text)
print pattern5.search(text).group()
print pattern5.search(text).group(0)
print pattern5.search(text).group(1)