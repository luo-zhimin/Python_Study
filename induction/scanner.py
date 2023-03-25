# 数据输入 input-scanner
"""
    数据输出：print
    数据输入：input

    使用input()语句可以从键盘获取输入
    使用一个变量接收（存储）input语句获取的键盘输入数据即可

    键盘输入何种类型的数据
    最终的结果都是：字符串类型的数据

"""
# 1
# print("请告诉我你是谁：")
# name = input()
# print(f"我叫{name}")

# 2
name = input("请告诉我你是谁：\n")
print(f"我知道了，你叫{name}")

age = input("请告诉我你的年龄：\n")
print(type(age))
print(f"我的年龄是{int(age)}")

# exercise 欢迎登陆小程序
"""
    定义两个变量，用以获取从键盘输入的内容，并给出提示信息：
    变量1，变量名：user_name，记录用户名称
    变量2，变量名：user_type，记录用户类型
"""
userName = input("请输入您的用户名：")
userType = input("请输入您的用户类型：")
print(f"您好{userName}欢迎光临，您是尊贵的{userType}会员")
