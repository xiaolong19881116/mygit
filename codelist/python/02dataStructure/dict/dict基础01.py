#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for dict"
 
__author__ = 'mxl'

#�ֵ�Ĵ�����ɾ��
dict_a = {'a':1,'b':2,'c':3}
keys = ['a','b','c','d']
values = [1,2,3,4]
dict_b = dict(zip(keys,values))
dict_c = dict(name = 'xiaolong',age = 28)
print dict_a
print dict_b
print dict_c

#�ֵ�Ԫ�صĻ�ȡ
print dict_c['name'] #ʹ���±꣬���±겻���ڣ��׳��쳣
print dict_c.get('addr') #�����ڣ�Ĭ�Ϸ���None
print dict_c.get('addr','China') #�����ڷ���ָ��ֵ
print dict_c.get('age','China')

#��ȡ��ʽ
for item in dict_c.items():
    print item 

for key,value in dict_c.items():
    print key,value

print dict_c.keys()
print dict_c.values()

#�ֵ�Ĳ�����ָ����ֵΪ�ֵ�Ԫ�ظ�ֵʱ�����ü�ֵ��������¸ü���Ӧ��ֵ�����������򴴽��µļ�ֵ��
dict_c['age'] = 29
dict_c['addr'] = 'China.HZ'
print dict_c

#ʹ��update������һ���ֵ��Ԫ��ȫ����ӵ���ǰ�ֵ�
print dict_a
print dict_c
dict_c.update(dict_a)
print dict_c