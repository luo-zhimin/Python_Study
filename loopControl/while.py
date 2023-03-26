"""
    while循环的基础语法
    while循环的基础案例
    while循环的嵌套应用
    while循环的嵌套案例
"""

# 基础语法
"""
    while 条件：
        条件满足时，要做的事情1
        ....
    
    注意点
        while的条件需得到布尔类型，True表示继续循环，False表示结束循环
        需要设置循环终止的条件，如i += 1配合 i < 100，就能确保100次后停止，否则将无限循环
        空格缩进和if判断一样，都需要设置
"""
# i = 0
# while i < 100:
#     print("小美，我喜欢你")
#     # i++ java c 语法
#     i += 1
#
# print("-----")
# # exercise
# # 求1-100的和
# i = 1
# result = 0
# while i <= 100:
#     result += i
#     i += 1
# print(f"1-100和为{result}")
# print("-----")
# # 基础案例
# """
#     设置一个范围1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数
#     无限次机会，直到猜中为止
#     每一次猜不中，会提示大了或小了
#     猜完数字后，提示猜了几次
# """
# loop = True
# i = 0
# result = random.randint(1, 100)
#
# while loop:
#     i += 1
#     name = input("请输入您要猜的数字：")
#     if name == '':
#         print("输入不可以为空，不可以转换数字～")
#     else:
#         number = int(name)
#         if number == result:
#             print("恭喜您，猜对了")
#             loop = False
#         else:
#             if number > result:
#                 print(f"您猜的数字大了")
#             else:
#                 print(f"您猜的数字小了")
# print(f"猜对了，一共猜了{i}次")
# print("------")
# # while循环的嵌套应用
# """
#     每天都去向小美表白直到成功为止
#     每次表白的流程是：送10朵玫瑰然后表白
#
#     同判断语句的嵌套一样，循环语句的嵌套，要注意空格缩进。
#     基于空格缩进来决定层次关系
#     注意条件的设置，避免出现无限循环（除非真的需要无限循环
# """
# i = 1
# while i <= 100:
#     # 每天都去向小美表白直到成功为止
#     print(f"今天是第{i}天，准备表白.....")
#     j = 1
#     while j <= 10:
#         print(f"送给小美的第{j}朵玫瑰花")
#         j += 1
#     print("小美我喜欢你～")
#     i += 1
# print(f"表白成功，今天是第{i - 1}天")

# while循环的嵌套案例
# print语句，输出不换行的功能
print("Hello", end='')
print("Word", end='')
print("\n九九乘法表")
i = 1
while i <= 9:
    # 重新赋值 从1开始
    j = 1
    while j <= i:
        # 对齐 不换行
        print(f"{i}*{j}={i * j}\t", end='')
        # 个数++
        j += 1
    # 行数++
    i += 1
    print()
