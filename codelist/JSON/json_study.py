import json
dict1 = {"name":"xianlong","age":28,"data":[1,2,3,4]}
print type(dict1),dict1
j1 = json.dumps(dict1) #���룺��һ��Python�������ת����Json�ַ���   json.dumps()
print j1
dict2 = json.loads(j1) # ��Json��ʽ�ַ�������ת����Python����   json.loads()
print type(dict2),dict2
print dict2["name"]