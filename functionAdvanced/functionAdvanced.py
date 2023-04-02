"""
    函数多返回值
        :return 多个值 逗号分隔
        按照返回值的顺序，写对应顺序的多个变量接收即可
        变量之间用逗号隔开
        支持不同类型的数据return

    掌握位置参数
        之前一直用的，位置一一匹配
    掌握关键字参数
        函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序
    掌握不定长参数
        位置
            传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组(tuple)，args是元组类型，这就是位置传递
        关键字
            参数是“键=值”形式的形式的情况下, 所有的“键=值”都会被kwargs接受, 同时会根据“键=值”组成字典
    掌握缺省参数
        函数入参有默认值，函数调用时，如果为缺省参数传值则修改默认参数值, 否则使用这个默认值
"""


def test_return():
    return 1, True, [1, 2, 3]


x, y, z = test_return()
print(f"x={x} y={y} z={z}")


# 位置参数
def location(province, city, district):
    return 1


def user_info(name, age, gender):
    print(f"您的名字是：{name},年龄是{age},性别{gender}")


# 关键字参数
user_info(name='小美', age=18, gender='男')
# 位置参数 + 关键字参数 可以混用 关键字参数可以乱序
user_info("小明", gender='女', age=20)


# 缺省参数
def province(x, y=100):
    print(f"当前经度为{x} 纬度为{y}")


# function has default value
province(100)
province(200, 1)


# 不定长参数
# 位置参数
def test_args(*args):
    print(f"args 的类型是{type(args)} ，内容是{args}")


# 关键字不定长
def test_keywords(**kwargs):
    print(f"kwargs 的类型是{type(kwargs)} ，内容是{kwargs}")


# 相当于java的...入参 ...(object) => tuple
test_args('1', 2, 3, True, [12, '3'])
# dict ==> Map
test_keywords(name='下', age=11, gender='女', pay=True)

# 匿名函数 inner function
