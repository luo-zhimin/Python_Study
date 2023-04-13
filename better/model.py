# 单例 single
"""
定义: 保证一个类只有一个实例,并提供一个访问它的全局访问点
适用场景:当一个类只能有一个实例，而客户可以从一个众所周知的访问点访问它时
"""
from str_tools import str_tools

# class StrTools:
#     pass
#
# str1 = StrTools()
# str2 = StrTools()
# print(f"str1:{id(str1)}\t\tstr2{id(str2)}")
s1 = str_tools
s2 = str_tools
print(f"s1:{id(s1)}\t\ts2{id(s2)}")


# factory
class Person:
    pass


class Worker(Person):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class Factory:
    def get_person(self, type):
        if type == 'w':
            return Worker
        elif type == 's':
            return Student
        else:
            return Teacher


f = Factory()
stu = f.get_person("s")
t = f.get_person("t")
work = f.get_person("w")
