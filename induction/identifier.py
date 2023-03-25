# 标识符

# 规则
"""
    标识符是用户在编程的时候所使用的一系列名字，用于给变量、类、方法等命名
    Python中，标识符命名的规则主要有3类：
        内容限定
        大小写敏感
        不可使用关键字
    标识符命名中，只允许出现：
        英文
        中文
        数字
        下划线（_）
    . 不推荐使用中文
    . 数字不可以开头
"""

# 内容限定
# error cloud not start with a number
# 1_name = "张三"
# name_ != "11"
# successful
_name = "张三"
name_ = "张三"

# 大小写敏感
Accept = "Accept"
accept = "accept"
print(Accept, accept)

# 不可使用关键字
# class = "class";
Class = "Class"
print(Class)

# 规范
"""
    见名知意
    下划线命名法
    英文字母全小写
"""
first_name = "john"
#
firstName = "john"
