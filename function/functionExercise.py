"""
    定义一个全局变量：money，用来记录银行卡余额（默认5000000）
    定义一个全局变量：name，用来记录客户姓名（启动程序时输入）
    定义如下的函数：
    查询余额函数
    存款函数
    取款函数
    主菜单函数
    要求：
    程序启动后要求输入客户姓名
    查询余额、存款、取款后都会返回主菜单
    存款、取款后，都应显示一下当前余额
    客户选择退出或输入错误，程序会退出，否则一直运行
"""

money = 5000000
name = None
loop = True

name = input("请输入您的名字进行登陆：")


# 定义查询函数
def query(show_header):
    if show_header:
        print("-----查询余额-----")
    print(f"{name},您好，您的余额剩余：{money}元")


# 定义存款
def saving(num):
    """
    :param num: 存款的金额
    :return:
    """
    global money
    money += num
    print("------存款-----")
    print(f"{name}，您好，您存款{num}成功")
    # 查询 参数控制是否输出表头
    query(False)


def get_money(num):
    """
       :param num: 取款的金额
       :return:
       """
    global money
    money -= num
    print("------请款-----")
    print(f"{name}，您好，您取款{num}成功")
    # 查询 参数控制是否输出表头
    query(False)


def menu():
    print("----主菜单----")
    print(f"{name}您好，欢迎来到ATM，请选择操作：")

    print("查询余额[输入1]")
    print("存款[输入2]")
    print("取款[输入3]")
    print("退出[输入4]")

    return int(input("请输入您的选择："))


# 设置无限循环
while loop:
    choose = menu()
    # 为了更好的实现 可以使用 continue ...
    if choose == 1:
        query(True)
        continue
    elif choose == 2:
        saving(int(input("请输入您要存款的金额：")))
        continue
    elif choose == 3:
        get_money(int(input("请输入您要取款的金额：")))
        continue
    else:
        loop = False
