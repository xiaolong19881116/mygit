#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for re"
 
__author__ = 'mxl'

#���õ�����Ԫ�ַ�
'''
. ƥ����˻�����������ⵥ���ַ�
* ƥ��λ��*ǰ��0�������ַ�
+ ƥ��λ��+ǰ��1�������ַ�
? ƥ��λ�ڣ�ǰ��1����0���ַ�
| ������
^ ƥ������
$ ƥ����β
[] ƥ��λ��[]������һ���ַ���ʾ��Χ
() ��λ��()�ڵ����ݵ���һ������Դ�
{} {m,n}ƥ���ظ�����m,n֮��
\b ����ͷ���ߵ���β; \B�����෴
\d ƥ������,[0-9];  \D�����෴
\s ƥ������հ׷�;   \S�����෴
\w ƥ����ĸ�����֡��»��� [a-zA-Z0-9_]; \W�����෴
'''

import re
  
#�ָ���б�
text = "xiaolong.xiao...yaya jyy"
patStr = '[\. ]+' #ע��һ���ո�
print re.split(patStr,text) #ʹ��reģ��ķ���
pattern = re.compile(patStr) #����ɶ�������ַ��������ٶ�
print pattern.split(text)

#����ȫ��
patStr2 = '[a-zA-Z]+'
print re.findall(patStr2,text)
pattern2 = re.compile(patStr2)
print pattern2.findall(text)

#�滻ģʽƥ���ַ���
patStr3 = '[xy]'
print re.sub(patStr3,'*',text)
pattern3 = re.compile(patStr3)
print pattern3.sub('@',text)

#ģʽƥ��match match���ַ�����ͷƥ�䣬��ͷƥ�䲻�ɹ�����None
patStr4 = 'xiao|long'
print re.match(patStr4,'xiao')
print re.match(patStr4,'xiao').group()

pattern4 = re.compile(patStr4)
print pattern4.match('long')
print pattern4.match('long').group()

print pattern4.match('lng')
#print pattern4.match('lng').group()

#ģʽƥ��search ƥ�������ַ���ֱ���ҵ�ƥ��
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