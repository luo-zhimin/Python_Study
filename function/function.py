"""
    介绍
        为了得到一个针对特定需求、可供重复利用的代码段
        提高程序的复用性，减少重复性代码，提高开发效率
    定义
        def 函数名(传入参数):
            函数体
            return 返回值
    函数调用
        函数名(参数)
        函数必须先定义后使用
    参数
        在函数进行计算的时候，接受外部（调用时）提供的数据
    返回值
        定义
            所谓“返回值”，就是程序中函数完成事情后，最后给调用者的结果
        注意
            函数体在遇到return后就结束了，所以写在return后的代码不会执行
        None
            如果函数没有使用return语句返回数据，那么函数有返回值吗？
            有的。

            Python中有一个特殊的字面量：None，其类型是：<class 'NoneType'>
            无返回值的函数，实际上就是返回了：None这个字面量

            None表示：空的、无实际意义的意思
            函数返回的None，就表示，这个函数没有返回什么有意义的内容。
            也就是返回了空的意思

        使用场景
            函数返回值
            if判断
                在if判断中，None等同于False
                一般用于在函数中主动返回None，配合if判断做相关处理
            变量定义
                定义变量，但暂时不需要变量有具体值，可以用None来代替
                name = None
    说明文档
        通过多行注释的形式，对函数进行说明解释
        内容应写在函数体之前
    嵌套调用
        在一个函数中，调用另外一个函数
        执行流程
            函数A中执行到调用函数B的语句，会将函数B全部执行完成后，继续执行函数A的剩余内容
    变量作用域
        变量作用域指的是变量的作用范围（变量在哪里可用，在哪里不可用）
        主要分为两类：局部变量和全局变量
        局部变量
            定义在函数体内部的变量，即只在函数体内部生效
            作用：在函数体内部，临时保存数据，即当函数调用完成后，则销毁局部变量
        全局变量
"""

# 不使用内置函数len()，完成字符串长度的计算
str1 = "test-prod"


# 最原始的直接多次复制使用
# count = 0
# for s in str1:
#     count += 1
# print(f"{str1}的长度为{count}")

# 定义一个函数
def my_len(data):
    count = 0
    for _ in data:
        count += 1
    print(f"字符串{data}长度为{count}")
    return count


def show():
    print("\n欢迎来到我的乐园\n祝你玩的开心，加油，你是最棒的\n前往不要迷失自己")


def add(x, y):
    """
    接收参数进行俩数相加
    ::param x 相加得数1
    ::param y 相加得数2
    ::return x+y
    """
    result = x + y
    print(f"{x}+{y}={result}")
    return result


"""
定义一个函数，名称任意，并接受一个参数传入（数字类型，表示体温）
在函数内进行体温判断（正常范围：小于等于37.5度）
"""


def check(temperature):
    print("欢迎来到自习室，由于是疫情期间，进来的时候请配和门卫量取体温，谢谢配合")
    if temperature >= 37.5:
        print(f"体温测量中，当前体温为{temperature}，体温异常，请远离，希望您回家自行隔离")
    else:
        print(f"体温测量中，当前体温为{temperature},体温正常请进！")


def say_hello():
    print("hello")
    return None


# 自己定义的函数
my_len(str1)

# exercise
show()

# params
print("---params---")
add(100, 200)

# params exercise
print("---params excise---")
check(37.5)
print()
check(35.5)

print("---")
# 返回值
re = add(5, 6)
print(f"add turn {re}")
# None
# 也可以自主返回None
print(f"无返回参数的类型是{type(say_hello())}")

# name = "Success"
name = None
# true not name = > name is empty
if not name:
    print("None")


# 函数说明文档

# 函数嵌套应用
def fun_1():
    print("---2--")


def fun_2():
    print("---1---")
    fun_1()
    print("---3---")


fun_2()

# 变量作用域
# 局部变量
num = 100

print()


def test():
    # 局部变量 修改 全局不生效
    # 使用 global关键字 可以在函数内部声明变量为全局变
    global num
    num = 1
    print(num)


# error not find because this num is global variable
# print(num)

# 全局变量
test()
# because global => num -> [test()->num]
print(num)

# exercise
