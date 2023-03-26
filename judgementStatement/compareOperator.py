# boolean and compare operation
"""
    布尔（bool）表达现实生活中的逻辑，即真和假
    True表示真
    False表示假
    True本质上是一个数字记作1，False记作0

    定义变量存储布尔类型数据
        变量名称 = 布尔类型字面量

    布尔类型不仅可以自行定义 同时也可以通过计算的来
    也就是使用比较运算符进行比较运算得到布尔类型的结果
"""

# 定义变量存储布尔类型数据
# true false
successful = True
error = False
print(f"successful内容是{successful},类型是{type(successful)}")
print(f"error内容是{error},类型是{type(error)}")

# 比较运算符
# == != > >= < <= (6种)
num1 = 10
num2 = 10
print(f"num1==num2的结果是{num1 == num2}")

num2 = 15
print(f"num1!=num2的结果是{num1 != num2}")

str1 = "test"
str2 = "prod"
print(f"str1==str2的结果是{str1 == str2}")

# > >= < <=
print(f"num1>num2的结果是{num1 > num2}")
print(f"num1>=num2的结果是{num1 >= num2}")
print(f"num1<num2的结果是{num1 < num2}")
print(f"num1<=num2的结果是{num1 <= num2}")
