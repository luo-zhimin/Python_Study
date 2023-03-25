# operator
"""
    算术（数学）运算符
    (+ - * / %)
    // -> 取整除  ** 指数 [a**b a的b次方]
    加（+）、减（-）、乘（*）、除（/）、整除（//）、取余（%）、求平方（**）
    赋值运算符
"""

# 算术（数学）运算符
print("1+1 =", 1 + 1)
print("2-1 =", 2 - 1)
print("2*1 =", 2 * 1)
print("4/2 =", 4 / 2)
print("9%2 =", 9 % 2)
# 整除
print("11//2 =", 11 // 2)
# 指数
print("2**3 =", 2 ** 3)
print("2*8 = %d" % (2 * 8))

# 赋值运算符
"""
    标准赋值： =
    复合赋值：+=、-=、*=、/=、//=、%=、**=
"""
# 标准赋值
num = 1 + 2 * 3
# 复合赋值
number = 1
number += 1  # number=number+1
number -= 1
number *= 4
number /= 2
print("number /= 2 = %d" % number)  # 2
number //= 2
number %= 2
print("number= %d" % number)  # 1
number **= 2
print("number **= 2 %d" % number)  # 1
