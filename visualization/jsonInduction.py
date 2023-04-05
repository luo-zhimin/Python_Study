"""
    JSON是一种轻量级的数据交互格式。可以按照JSON指定的格式去组织和封装数据
    JSON本质上是一个带有特定格式的字符串
    json.dumps 对象转换为json
    json.loads json转化为dict
"""
# 导入json包
import json

# 准备列表 嵌套字典 进行Json转换
# dict list
data = [{"name": "张三", "age": 13}, {"name": "里斯", "age": 20}, {"name": "王武", "age": 22}]
# ensure_ascii 中文 false 不使用ascii码进行转换
data_json = json.dumps(data, ensure_ascii=False)
print(f"data_json 类型是{type(data_json)},内容是{data_json}")

# 准备字典 将字典转换为Json
d = {"name": "周杰伦", "address": "台北"}
d_json = json.dumps(d, ensure_ascii=False)
print(f"d_json 类型是{type(d_json)},内容是{d_json}")

# 将json字符串转换为json数据类型 key:value
really_json = '[{"name": "张三", "age": 13}, {"name": "里斯", "age": 20}, {"name": "王武", "age": 22}]'
really_data = json.loads(really_json)
print(f"really_data 类型是{type(really_data)},内容是{really_data}")

# 将json字符串转换为python数据类型{k:v,k:v}
dict_json = '{"name": "周杰伦", "address": "台北"}'
dict_data = json.loads(data_json)
print(f"dict_data={dict_data}")
