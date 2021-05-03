'''json'''
import json
#是把json格式的字符串转化成python当中的字典,反序列化
a='{"username":"yuz","age":10}'
print(json.loads(a))

#python的字典转化成json格式的字符串，序列化
b={"name":"星河","age":3}
print(json.dumps(b))