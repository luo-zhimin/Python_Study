# 数据类型
"""
    掌握使用type()语句查看数据的类型
    理解变量无类型而数据有类型的概念
"""

# type(被查看类型的数据)
# 直接输出类型信息
print(type("test"))
print(type(11))
print(type(11.11))
print("-----")
# 用变量存储type()的结果（返回值
string_type = type("prod")
int_type = type(22)
float_type = type(22.22)
print(string_type)
print(int_type)
print(float_type)
print("-----")
# 用变量存储type()的结果（返回值
name = "study"
name_type = type(name)
print(name_type)

# string 3种方式
# 双引号定义法
text1 = "text1"
# 单引号定义法
text2 = 'text2'
# 三引号定义法 要注意的是，包含范围是：从三个引号开始，到下一个三个引号结束
text3 = """text3"""

# 数据类型转换 transformQuantityType
# 掌握如何在字符串、整数、浮点数之间进行相互转换 了解转换的注意事项

# int(x) float(x) str(x) have return value
# !!!
# 1. 任何类型，都可以通过str()，转换成字符串
# 2. 字符串内必须真的是数字，才可以将字符串转换为数字

# 将数字转换为字符串
print("----")
name_str = "name"
print(type(name_str), name_str)

tInt = int("11")
print(tInt)

# error 字符串内必须真的是数字
# print(int(name_str))

tFloat = float("11")
t2Float = float("11.11")
print(tFloat, t2Float)

# int -> float
iFloat = float(2)
print(iFloat)

"""
    homework
    定义4个变量，需求：姓名：孙悟空，年龄：600岁，技能：筋斗云、72变，主要战绩：大闹天宫
    定义变量，c1 = '可乐'，c2 = '牛奶'，通过Python代码把c1内容调整为牛奶，c2调整为可乐。（提示：两个数的交换）
"""
name = "孙悟空"
age = 600
technicalAbility = "筋斗云、72变"
militaryExploits = "大闹天宫"

c1 = '可乐'
c2 = '牛奶'
print(c1, c2)
# exchange
temp = c1
c1 = c2
c2 = temp
print(c1, c2)
