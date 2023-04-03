"""
    exception
        异常就是程序运行的过程中出现了错误
    异常处理（捕获异常）
        提前假设某处会出现异常，做好提前准备，当真的出现异常的时候，可以有后续手段
        语法
            try
                可能出现的错误
            except
                出现后执行的东西
        捕获指定异常
            except exceptionName as constant
            如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常
        捕捉多个异常
            except (firstExceptionName,secondExceptionName,...) as e
            need tuple write
            捕获多个异常时，可以把要捕获的异常类型的名字，放到except 后，并使用元组的方式进行书写
"""
# exception
# No such file or directory: 'hello'
try:
    # f = open("hello", 'r')
    print(1 / 0)
# catch exception
# except:
# 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常
# 当捕获多个异常时，可以把要捕获的异常类型的名字，放到except 后，并使用元组的方式进行书写
except (FileNotFoundError, ZeroDivisionError) as e:
    f = open('exception.py', 'r')
    print("this file or directory no such")
    # write abnormal cause
    # division by zero
    print(e)
else:
    print("我是没有异常，执行的代码～～")
finally:
    # 表示的是无论是否异常都要执行的代码，例如关闭文件
    # 执行比如说关闭文件等 文件流 file stream
    print("一定会执行的代码～")


# 异常传递
def fun1():
    print("1 start")
    num = 1 / 0  # zero exception
    print("1 end")


def fun2():
    print("2 start")
    # need catch
    try:
        fun1()
    except Exception as e:
        print(e)
    # execute
    print("2 end")


def main():
    try:
        fun2()
    except Exception as e:
        print(e)


main()
