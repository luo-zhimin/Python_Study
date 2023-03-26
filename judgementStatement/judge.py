# 判断语句
"""
    if 要判断的条件：
        条件成立时，要做的事情

    判断语句的结果，必须是布尔类型True或False
    True会执行if内的代码语句
    False则不会执行
"""
import random

age = 30

# 归属于if判断的代码语句块，需在前方填充4个空格缩进
# Python通过缩进判断代码块的归属关系
if age >= 18:
    print("你已经成年了！")
    print(f"你现在{age}岁了")

print("不，我不想成年")
print("----if exercise---")
# if exercise
"""
    通过input语句，获取键盘输入，为变量age赋值。（注意转换成数字类型）
    通过if判断是否是成年人，满足条件则输出提示信息
"""
print("欢迎来到游乐场，儿童免费，成人收费")
age = input("请输入你的年龄：")
if int(age) >= 18:
    print("您已成年，需要补票价10元")
print("祝您游戏愉快！")
print("-------")

# if else 语句
"""
    else后，不需要判断条件
    和if的代码块一样，else的代码块同样需要4个空格作为缩进
"""

age = 20
if age <= 18:
    print("祝您童年愉快～")
else:
    print("祝您工作愉快，事业有成～")

# if else exercise
"""
    通过input语句获取键盘输入的身高
    判断身高是否超过120cm，并通过print给出提示信息
"""
print("----if else exercise---")
print("欢迎来到天星动物园")
height = input("请输入你的身高(cm): ")
if int(height) > 120:
    print("您的身高超过120cm，游玩需要补票10元")
else:
    print(f"您现在身高为{height}cm，可以免费游玩")
print("祝您游玩愉快")

# if elif else语句
print("--------")
"""
    某些场景下，判断条件不止一个，可能有多个
    判断是互斥且有顺序的。
    满足1 将不会理会2和3
    满足2 将不会理会3
    1、2、3均不满足，进入else
    else也可以省略不写，效果等同3个独立的if判断
    空格缩进同样不可省略
"""
print("欢迎来到梦想城")
height = int(input("请输入你的身高(cm): "))
vip_level = int(input("请输入你的vip等级(1-5): "))
day = int(input("请输入今天的日期(1-30)："))
if height < 120:
    print(f"您现在身高为{height}cm，可以免费游玩")
elif vip_level > 3:
    print(f"您的vip等级为{vip_level}，可以免费游玩")
elif day == 1:
    print("今天是1号免费日")
else:
    print("不要意思，您需要购票花费10元")
print("祝您游玩愉快")

# if elif else exercise
print("----if elif else exercise---")
"""
    定义一个变量，数字类型，内容随意
    基于input语句输入猜想的数字，通过if和多次elif的组合，判断猜想数字是否和心里数字一致
"""
number = 10
if number == int(input("请输入第一次猜想的数字：")):
    print(f"猜对了，我想的就是{number}")
elif number == int(input("不对，猜错了，在猜一次：")):
    print("猜对了")
elif number == int(input("不对，再猜最后一次：")):
    print("猜对了")
else:
    print("Sorry,猜错了～")
print("--------")
# 判断语句的嵌套
"""
    有很多场景，不仅仅是多个并列条件，还会有满足前置条件才会二次判断的多层判断需求
    基本语法
        if 条件1：
            满足条件1 做的事情1
            满足条件1 做的事情2
            if 条件2：
                满足条件2 做的事情1
                满足条件2 做的事情2

    嵌套的关键点，在于：空格缩进
    通过空格缩进，来决定语句之间的：层次关系

    公司要发礼物，条件是：
    1. 必须是大于等于18岁小于30岁的成年人
    2. 同时入职时间需满足大于两年，或者级别大于3才可领取
"""
age = int(input("请输入您的年龄："))
year = int(input("请输入您的入职年限："))
level = int(input("请输入您的级别："))
if 18 < age < 30:
    print("年龄满足")
    if year >= 2 or level >= 3:
        print("您满足条件，可以领取礼物")
    elif year < 2:
        print("司龄不满足")
    else:
        print("级别不符合")
else:
    print("年龄不符合")

# excise
"""
    数字随机产生，范围1-10
    有3次机会猜测数字，通过3层嵌套判断实现
    每次猜不中，会提示大了或小了
"""
number = random.randint(1, 10)

# 建议循环～简单 快捷
guess_num = int(input("输入你要猜的数字："))

if number == guess_num:
    print("恭喜，第一次就猜到了")
else:
    if number > guess_num:
        print(f"你要猜的数字小了，当前值为{number}")
    else:
        print(f"你要猜的数字大了，当前值为{number}")

    guess_num = int(input("再次输入你要猜的数字："))

    if number == guess_num:
        print("恭喜，第二次就猜到了")
    else:
        if number > guess_num:
            print(f"你要猜的数字小了，当前值为{number}")
        else:
            print(f"你要猜的数字大了，当前值为{number}")

        guess_num = int(input("最后一次，输入你要猜的数字："))

        if number == guess_num:
            print("恭喜，第三次就猜到了")
        else:
            print("机会已经用完了")
