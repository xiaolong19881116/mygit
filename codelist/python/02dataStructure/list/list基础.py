#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for list"
 
__author__ = 'mxl'

#�б�Ĵ�����ɾ��
list_a = ['a','b','xyz']
#range(start,stop,step),startĬ��Ϊ0��stop(����в��������ֵ)������Ĭ��Ϊ1
list_b = range(2,11,2) 
print list_b
#ɾ���б�
del list_a

#�б�Ԫ�ص�������ɾ��
list_b = list_b + [12] #�÷�ʽ�ᴴ��һ���µ��б���
print list_b
list_b.append(14) #���������ϵ���β�����Ԫ�أ���ԭ��ַ�޸��б��ٶȿ죬�Ƽ�ʹ��
print list_b
list_b.extend([16,18]) #ͬ��extend����Ҳ��ԭ�ز���
print list_b
list_b.insert(3,30) #��ָ��λ�����Ԫ��
print list_b
print list_b[0] #���ʵ�һ��Ԫ��
print list_b[1] #���ʵڶ���Ԫ��
print list_b[-1] #�������һ��Ԫ��

del list_b[3] #ɾ��ָ��λ���ϵ�Ԫ��
print list_b
list_b.pop(2) #ɾ��ָ��λ���ϵ�Ԫ��,Ĭ�����һ��
print list_b
list_b.pop()
print list_b

list_c = [1,1,23,568,88,88,12,0,88]
print list_c.count(88) #����ָ��Ԫ�����б��г��ֵĴ���
print list_c
list_c.remove(88) #ɾ���״γ��ֵ�ָ��Ԫ��
print list_c
print list_c.count(88) #����ָ��Ԫ�����б��г��ֵĴ���

print 23 in list_c #��Ա�ʸ��ж�
print 13 in list_c

#�б�����
list_d = [3,4,5,6,7,9,11,13,15,17,19,23]
import random
random.shuffle(list_d) #����˳��,ֱ�Ӳ����б�
print list_d

list_d.sort() #Ĭ����������
print list_d
list_d.sort(reverse = True)
print list_d
list_d.sort(key = lambda x:len(str(x))) #�Զ�������
print list_d

'''
���ú���sorted()���б�����������б�����sort()������ͬ��
�ú��������µ��б�����ԭ�б�����κ��޸�
ͬ��
���ú���reversed()���б��������,����һ�������ĵ����������б�����reverse()������ͬ��
�ú��������µ��б�����ԭ�б�����κ��޸�
'''
alist = [1,3,7,5,4]
print sorted(alist)
print alist
print reversed(alist)
print list(reversed(alist) )
print alist

#���ú���
'''
zip
'''
alist = [1,2,3]
blist = [4,5,6]
clist = [7,8,9]
dlist = zip(alist,blist,clist)#���б��Ԫ���Ӧλ��Ԫ����ϳ�Ԫ�飬�����ذ�����ЩԪ����б�
print dlist

'''
enumerate �����±��Ԫ��ֵ��Ԫ��
'''
alist = ['a','b','c']
for index,value in enumerate(alist):
    print index,value

'''
 �б��Ƶ�ʽ
'''

print [x**2 for x in range(2,11,2)]
print [x+y for x in 'ABC' for y in 'ABC']
print [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]

