#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for jieba"

import jieba
 
seg_list = jieba.cut("�����������廪��ѧ", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # ȫģʽ
 
seg_list = jieba.cut("�����������廪��ѧ", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # ��ȷģʽ
 
seg_list = jieba.cut("�����������廪��ѧ")
print("Default Mode2: " + "/ ".join(seg_list))  # ��ȷģʽ
 
seg_list = jieba.cut("�����������׺��д���")  # Ĭ���Ǿ�ȷģʽ
print(", ".join(seg_list))
 
seg_list = jieba.cut_for_search("С��˶ʿ��ҵ���й���ѧԺ�������������ձ�������ѧ����")  # ��������ģʽ
print("* ".join(seg_list))