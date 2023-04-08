"""
    初识对象

    def methodsName(self,xx,xx):
        methodBody
    在方法定义的参数列表中，有一个：self关键字 self关键字是成员方法定义的时候，必须填写的
    它用来表示类对象自身的意思
    当我们使用类对象调用方法的是，self会自动被python传入
    在方法内部，想要访问类的成员变量，必须使用self
"""


# 设计一个类
class Student:
    # 类中定义的属性（变量），我们称之为：成员变量
    # 学生名字
    name = None
    # 性别
    gander = None
    # 国籍
    nationality = None,
    # 籍贯
    native_place = None
    # 年龄
    age = None

    # 类中定义的行为（函数），我们称之为：成员方法
    def speckStudentName(self):
        print(f"大家好呀，我是{self.name}")

    # 在传入参数的时候，self是透明的，可以不用理会它
    def speckStudentNameByName(self, name):
        print(f"大家好呀，我是{name}")


# 创建一个对象
stu1 = Student()
# 赋值 assignment
stu1.name = '张三'
stu1.gander = '男'
stu1.nationality = 'china'
stu1.native_place = '山东'
stu1.age = 11
# 获取value
# ....
print(stu1.name)
# 调用类的方法
stu1.speckStudentName()
print("----")
stu1.speckStudentNameByName("王武")
