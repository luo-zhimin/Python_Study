# 基础匹配
import re

# match(匹配规则， 被匹配字符串)
s = "python itheima"
result = re.match("python", s)
print(result)
# index
print(result.span())  # (0,6)
# words
print(result.group())
# math 从头开始
s = "1python python python"
result = re.match('python', s)
print(result)  # None

# 搜索整个字符串，找出匹配的。从前向后，找到第一个后，就停止，不会继续向后
# search(匹配规则， 被匹配字符串)
search_result = re.search('python', s)
print(search_result)  # (1,7)
print(re.search('it', s))  # None

# findall(匹配规则， 被匹配字符串)
# 匹配整个字符串，找出全部匹配项
any_result = re.findall('python', s)
print(any_result)

# 元字符匹配
s = "theima1 @@python2 !!666 ##itcast3"
# 字符串前面带r的标记 表示字符串转义符号无效 是普通字符
any_result = re.findall(r'\d', s)
print(any_result)
# 匹配账号，只能由字母和数字组成 长度为6-10
account = 'dajsla121q'
r = '^[0-9|A-z]{6,10}$'
first = re.findall(r, account)
print(first)

# 匹配qq号 纯数字 长度5-11，第一位不为0
r = '^[1-9]?[0-9]{4,10}$'
qq = '1798677862'
second = re.findall(r, qq)
print(second)
# 匹配邮箱地址 只允许qq，163，gmail这三种邮箱地址
# 1798677862@qq.com => {内容}.{内容}@{内容}.{内容}
# ^[\w-]+ {+一次或者多次} \w =》[0-9A-z]
# findall 如果带括号外面需要带一个括号 不然就是分开几组
r = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
em = "1798677862@qq.com"
third = re.match(r, em)
print(third.group())
