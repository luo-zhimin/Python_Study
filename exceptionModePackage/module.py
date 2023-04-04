"""
    module
        Python 模块(Module)，是一个 Python 文件，以 .py 结尾.  模块能定义函数，类和变量，模块里也能包含可执行的代码
    作用
            python中有很多各种不同的模块, 每一个模块都可以帮助我们快速的实现一些功能, 比如实现和时间相关的功能就可以使用time模块
        我们可以认为一个模块就是一个工具包, 每一个工具包中都有各种不同的工具供我们使用进而实现各种不同的功能.
    基本语法
        import模块名
            import 模块名1，模块名2
        from 模块名 import 功能名
    注意事项：当导入多个模块的时候，且模块内有同名功能. 当调用这个同名功能的时候，调用到的是后面导入的模块的功能

"""
# # 模块定义别名
import random as r
# 使用from 导入time的sleep
# from time import sleep
# 引入这个模块的这个所有功能 和上面那个import几乎一样但是写法不一样
from time import *

# import my_module
from my_module import *

# 导入
# import time  # 导入Python内置的模块
#
# # 使用模块的函数
# # sleep seconds
# print("你好")
# time.sleep(10)  # 通过.就可以使用模块内部的所有功能
# print("我是未来的你")

print(r.randint(1, 10))
print("我是1s前的你")
sleep(1)
print("我是1s后的你")

# __main__
# my_module.sumNumber(2, 3)

# __all__
sumNumber(3, 3)
# divNumber(2, 2)
