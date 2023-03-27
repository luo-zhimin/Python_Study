# 基本语法
"""
    while循环的循环条件是自定义的，自行控制循环条件
    for循环是一种”轮询”机制，是对一批内容进行”逐个处理”

    for 临时变量 in 待处理数据集:
        循环满足条件时执行的代码
"""

name = "family"
# 同while循环不同，for循环是无法定义循环条件的。
# 只能从被处理的数据集中，依次取出内容进行处理
for n in name:
    print(n)

# 数一数有几个a
name = "itheima is a brand of itcast"
count = 0
for n in name:
    if n == 'a':
        count += 1
print(f"{name} 一共{count}个a")

# range
"""
    for 临时变量 in 待处理数据集(可迭代对象): 
         循环满足条件时执行的代码
         
    语法中的：待处理数据集，严格来说，称之为：可迭代类型
    可迭代类型指，其内容可以一个个依次取出的一种类型 包括：
    字符串，列表，元组，等
    
    range 获得一个简单的数字序列（可迭代类型的一种）
    range(num)
        获取一个从0开始，到num结束的数字序列（不含num本身）
    range(num1，num2)
        获得一个从num1开始，到num2结束的数字序列（不含num2本身）
    range(num1, num2, step)
        获得一个从num1开始，到num2结束的数字序列（不含num2本身）数字之间的步长，以step为准（step默认为1）
"""
# 0-4
# for r in range(5):
# 1-4 获得一个从num1开始，到num2结束的数字序列
# for r in range(1, 5):
# 1,3,5..9 [2为step]
for r in range(1, 10, 2):
    print(r)
print("------")
# range excise
"""
    定义一个数字变量num，内容随意
    并使用range()语句，获取从1到num的序列，使用for循环遍历它。
    在遍历的过程中，统计有多少偶数出现
"""
number = 100
count = 0
for n in range(1, number):
    if n % 2 == 0:
        count += 1
print(f"1到{number}中，一共{count}个偶数")

print("----")
# 变量作用域
"""
   for i in range(2):
    print(i)
print(i)

临时变量，在编程规范上，作用范围（作用域），只限定在for循环内部
实际上是可以访问到的
在编程规范上，是不允许、不建议这么做的
"""

# for循环的嵌套应用
# 小美表白
i = 0
for i in range(1, 101):
    print(f"今天是第{i}天，坚持")
    for j in range(1, 11):
        print(f"送给小美的第{j}朵花")
    print(f"小美我喜欢你，(第{i}天表白结束)")
print(f"第{i}天表白成功～")
print("------")
# for 9*9
for i in range(1, 10):
    # 因为要包含他所以需要+1
    for j in range(1, i + 1):
        print(f"{i}*{j}={i * j}\t", end='')
    print()
