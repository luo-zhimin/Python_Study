"""
    continue 临时跳过(中断本次循环，直接进入下一次循环)
    break 直接结束
    for循环和while循环，效果一致
"""
import random

for i in range(1, 5):
    print(f"今天是第{i}天，坚持")
    print("给小美送早饭，比心")
    print("给小美送午饭，比心")
    if input(f"今天小美的心情好想(0好心情 1坏心情)：") == '1':
        print("今天小美心情不好撤退～")
        continue
    if input(f"小美告诉我，你是否明确拒绝(0再观察一下 1直接拒绝)：") == "1":
        print("小美拒绝了我，以后不在追求了😭")
        break
    print("给小美送晚饭，回家并表白")

# exercise
"""
    某公司，账户余额有1W元，给20名员工发工资。
    员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元
    领工资时，财务判断员工的绩效分（1-10）（随机生成），如果低于5，不发工资，换下一位
    如果工资发完了，结束发工资。
"""
money = 10000
for m in range(1, 21):
    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{m}，你的绩效为{score}，当月不及格，工资停止发放")
        continue
    else:
        money -= 1000
        print(f"向第{i}个员工发发工资1000元,剩余{money}元")
        if money == 0:
            print("工资发放完毕，请等待下个月")
            break
print("大家继续加油")
