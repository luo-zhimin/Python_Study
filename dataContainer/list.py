"""
    数据容器
        就是为了批量存储或批量使用多份数据
        一种可以容纳多份数据的数据类型，容纳的每一份数据称之为1个元素
        每一个元素，可以是任意类型的数据，如字符串、数字、布尔等。

        数据容器根据特点的不同，如：
        是否支持重复元素
        是否可以修改
        是否有序，等
        分为5类，分别是：
        列表（list）、元组（tuple）、字符串（str）、集合（set）、字典（dict）

        list
            列表内的每一个数据，称之为元素
            以 [] 作为标识
            列表内每一个元素之间用, 逗号隔开
        列表可以一次存储多个数据，且可以为不同的数据类型，支持嵌套

        可以通过index去取数据
            正向 从0开始
            逆向 从-1开始
        注意
            一定要在有效的位置内进行取值(小心数组越界) numberOutOfBound
"""
# 列表可以一次存储多个数据，且可以为不同的数据类型，支持嵌套
# Python 是一种弱语言 支持一个list里面放置多种数据类型
name_list = ["prod", "test", "gpa", "java"]
print(name_list)
print(f'name_list的格式是{type(name_list)}')
# 同时也支持嵌套 在其他语言方面称为多维数组
number_list = [[1, 2, 3], [2, 3, 4]]
print(number_list)
print(f'number_list的格式是{type(number_list)}')

# index => find value by index [array/list]
# 反向取Python 单独支持
# 正向取数据
print("--正向数据--")
print(name_list[0])
print(name_list[1])
# 逆向数据
print("---逆向数据----")
print(name_list[-1])
# 嵌套list取数据 原理就是 array inner array find one array stackOver
print("--嵌套list取数据--")
print(f"取出嵌套数据第一层{number_list[0]}")
# 多维数组
print(f"取出嵌套数据第一层的在下一级:{number_list[0][0]}")

"""
    常用操作
        插入元素
        删除元素
        清空列表
        修改元素
        统计元素个数
"""
"""
查找某元素的下标
     功能：查找指定元素在列表的下标，如果找不到，报错ValueError
     语法：列表.index(元素)
     index就是列表对象（变量）内置的方法（函数）
"""
print("----常用操作-----")
# ValueError value not find in array
# print(name_list.index("111"))
# 查找
print(f"查找prod在下标为{name_list.index('prod')}的位置下")
# 修改
# 语法：列表[下标] = 值
# 可以使用如上语法，直接对指定下标（正向、反向下标均可）的值进行：重新赋值（修改）
print("----修改---")
name_list[0] = "Python"
# prod -> Python
print(name_list)
name_list[-3] = "C++"
# test -> C++
print(name_list)
# insert
print("--insert--")
# 语法：列表.insert(下标, 元素)，在指定的下标位置，插入指定的元素
name_list.insert(2, "Go")
print("--append--")
# 列表.append(元素)，将指定元素，追加到列表的尾部
# 追加一个
name_list.append("Spring")
# 追加一批
# 语法：列表.extend(其它数据容器)，将其它数据容器的内容取出，依次追加到列表尾部
name_list.extend(["Cloud", "Mvc", "Kafka", "RabbitMQ"])
print(f"insert and append result -> {name_list}")
# 删除
# 语法1： del 列表[下标]
del name_list[3]
print(f"del array -> {name_list}")
# 语法2：列表.pop(下标)
# =>Java stack pop 弹出
p = name_list.pop(-3)
print(f"name list pop -3 -> {p}")
# 删除某元素在列表中的第一个匹配项
# 语法：列表.remove(元素)
# Java list remove object
name_list.remove("java")
print(f"remove result -> {name_list}")
# 清空列表内容，语法：列表.clear()
number_list.clear()
print(f"clear result ->{number_list}")
# 统计某元素在列表内的数量
# 列表.count(元素)
count = name_list.count("Go")
print(f"name list count->{count}")
# 统计列表内，有多少元素
print(f"name list length {len(name_list)}")

print("\n------\n")
"""
有一个列表，内容是：[21, 25, 21, 23, 22, 20]，记录的是一批学生的年龄

    请通过列表的功能（方法），对其进行
    定义这个列表，并用变量接收它
    追加一个数字31，到列表的尾部
    追加一个新列表[29, 33, 30]，到列表的尾部
    取出第一个元素（应是：21）
    取出最后一个元素（应是：30）
    查找元素31，在列表中的下标位置

"""

exercise = [21, 25, 21, 23, 22, 20]
exercise.append(31)
print(f"1->{exercise}")
exercise.extend([29, 33, 30])
print(f"2->{exercise}")
r = exercise[0]
print(f"3->{r}")
# p = exercise.pop()
p = exercise[-1]
print(f"4->{p}")
i = exercise.index(31)
print(f"5->{i}")

print("\n------\n")

"""
    while循环和for循环的对比
    while循环和for循环，都是循环语句，但细节不同：
    在循环控制上：
        while循环可以自定循环条件，并自行控制
        for循环不可以自定循环条件，只可以一个个从容器内取出数据
    在无限循环上：
        while循环可以通过条件控制做到无限循环
        for循环理论上不可以，因为被遍历的容器容量不是无限的
    在使用场景上：
        while循环适用于任何想要循环的场景
        for循环适用于，遍历数据容器的场景或简单的固定次数循环场景
"""


# foreach
def list_while():
    index = 0
    print("list_while")
    while index <= len(exercise):
        print(exercise[index])
        index += 1


def list_foreach():
    print("list_foreach")
    for e in exercise:
        print(e)


# list_while()
list_foreach()

"""
    定义一个列表，内容是：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    遍历列表，取出列表内的偶数，并存入一个新的列表对象中
    使用while循环和for循环各操作一次
"""
i = 0
temp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
# while i < len(temp):
#     if temp[i] % 2 == 0:
#         result.append(temp[i])
#     i += 1
# print(result)

for r in temp:
    if r % 2 == 0:
        result.append(r)
print(result)
