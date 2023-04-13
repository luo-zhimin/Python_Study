# 装饰器
# 闭包

# def outer(fun):
#     def inner():
#         print("我睡觉了")
#         fun()
#         print("我起床了")
#
#     return inner
#
#
# def sleep():
#     import random
#     import time
#     print("睡眠中....")
#     time.sleep(random.randint(1, 5))
#
#
# # sleep()
# # init
# sl = outer()
# # running inner
# sl()


def outer(fun):
    def inner():
        print("我睡觉了")
        fun()
        print("我起床了")

    return inner


@outer
def sleep():
    import random
    import time
    print("睡眠中....")
    time.sleep(random.randint(1, 5))


sleep()
