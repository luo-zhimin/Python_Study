"""
    闭包
"""


# 简单闭包
# def outer(logo):
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner

# o = outer("hello")
# o("word")
# o("dream")

# 用nonlocal关键字修改外部函数的值
# def outer(num1):
#     def inner(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#
#     return inner

# n = outer(10)
# n(1)
# n(12)
# n(13)

# ATM
def account_creat(init_money=0):
    def atm(num, deposit=True):
        nonlocal init_money
        if deposit:
            init_money += num
            print(init_money)
        else:
            init_money -= num
            print(init_money)

    return atm


ac = account_creat(100)
# add
ac(100)
ac(200)
# sub
ac(100, deposit=False)
