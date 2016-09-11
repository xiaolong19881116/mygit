import json
dict1 = {"name":"xianlong","age":28,"data":[1,2,3,4]}
print type(dict1),dict1
j1 = json.dumps(dict1) #编码：把一个Python对象编码转换成Json字符串   json.dumps()
print j1
dict2 = json.loads(j1) # 把Json格式字符串解码转换成Python对象   json.loads()
print type(dict2),dict2
print dict2["name"]