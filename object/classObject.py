"""
    类和对象
    类创建对象的语法
        对象名=类名称()
    Construction
        __init__
"""
# import winsound


# 设计一个闹钟类
class Clock:
    id = None
    price = None

    def ring(self):
        # 声音大小 时间长短
        # os.system()
        print(f"os linux ring")
        # 只有windows支持
        # winsound.Beep(2000, 3000)


clock1 = Clock()
clock1.id = 1
clock1.price = 19.99
print(f"闹钟编号:{clock1.id},价格:{clock1.price}")
clock1.ring()


# ....
class Student:
    # 有构造方法 可以省略
    # name = None
    # age = None
    # tel = None

    # 在创建类对象（构造类）的时候，会自动执行。
    # 在创建类对象（构造类）的时候，将传入参数自动传递给__init__方法使用
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        # order 1
        print("Student类创建了一个类对象")


# 含参
stu = Student("张三", 11, 12345678912)
print(f"student {stu.name}-{stu.age}-{stu.tel}")
# 无参
# stu1 = Student()
# print(stu1)

# exercise
"""
开学了有一批学生信息需要录入系统，请设计一个类，记录学生的：
姓名、年龄、地址，这3类信息
请实现：
通过for循环，配合input输入语句，并使用构造方法，完成学生信息的键盘录入
输入完成后，使用print语句，完成信息的输出
"""


class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        print("student init~")


number = 10
for n in range(1, number + 1):
    print(f"当前录入第{n}名学生的信息，一共{number}名学生")
    name = input("请输入学生的姓名：")
    age = input("请输入学生的年龄：")
    address = input("请输入学生的地址：")
    stu = Student(name, age, address)
    print(f"学生{n}录入完成，信息为['姓名':{stu.name},'年龄':{stu.age},'地址':{stu.address}]")
