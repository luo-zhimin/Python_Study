"""
    类型注解

    变量的类型注解
    函数（方法）形参列表和返回值的类型注解
"""
import random
from typing import Union

# 基础数据类型注解
var_1: int = 10
var_2: str = 'str'


# 类对象类型注解
class Student:
    pass


stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2]
my_tuple: tuple = (1, 2)
my_dict: dict = {"value": 11}

# detail
my_list: list[int] = [1, 2]
my_tuple: tuple[int, int] = (1, 2)
my_dict: dict[str, int] = {"value": 11}

# 在注释中进行类型注解
int_1 = random.randint(1, 10)  # type:int


# function annotations (params,return)
def add(x: int, y: int) -> int:
    return x + y


print(add(2, 3))


def fun(data: list) -> list:
    # pass
    return data


print(fun([1, 2, 3]))

# union
# un_list: list[int, str] = [1, 2, 3, '222']
un_list: list[Union[int, str]] = [1, 2, 3, '222']


def func(data: Union[int, str]) -> Union[int, str]:
    pass


func()
