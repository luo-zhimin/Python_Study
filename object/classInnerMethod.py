"""
    内置方法
    __init__
    __lt__  < >
    __le__ <= >=
    __eq__ ==
    __str__ string
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # toString override 不重写的话返回的是内存地址
    def __str__(self):
        return f"Student类对象，name:{self.name},age:{self.age}"

    # lt gt < >
    def __lt__(self, other):
        return self.age < other.age

    # le <= >=
    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age


stu = Student("周杰伦", 31)
stu1 = Student("林俊杰", 21)
print(stu)
print(str(stu))

# lt
# 31 < 21
print(stu < stu1)
# 31 > 21
print(stu > stu1)

# le
# 31 < 21
print(stu <= stu1)
# 31 > 21
print(stu >= stu1)

# eq
print(stu == stu1)
# True  NotImplemented(__eq__) need impl eq class override eq
print(stu1.__eq__(Student("林俊杰", 21)))
