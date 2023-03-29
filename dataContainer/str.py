name = "hello"
# 同元组一样，字符串是一个：无法修改的数据容器
# 如果必须要做，只能得到一个新的字符串，旧的字符串是无法修改
print(f"{name}的 1 号下标是{name[1]}")
print(f"{name}的 -1 号下标是{name[-1]}")
# 查找特定字符串的下标索引值
# 语法：字符串.index(字符串)
print(f"{name}的 h 下标是{name.index('h')}")

# 字符串的替换
#      语法：字符串.replace(字符串1，字符串2）
#      功能：将字符串内的全部：字符串1，替换为字符串2
#      注意：不是修改字符串本身，而是得到了一个新字符串哦
new_name = name.replace('l', 'w')
print(f"name replace new_name => {new_name}")

# 字符串的分割
#      语法：字符串.split(分隔符字符串）
#      功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
#      注意：字符串本身不变，而是得到了一个列表对象
really_data = " I want to have a cat or a dog because it's very lovely "
really_data_array = really_data.split(" ")
print(f"really_data_array = > {really_data_array}")

# 字符串的规整操作（去前后空格）
#      语法：字符串.strip()
# 字符串的规整操作（去前后指定字符串）
#      语法：字符串.strip(字符串)

# 不穿入参数去除前后空格
print(really_data.strip())
# print(really_data.strip('t'))

name.count('a')

len(name)

my_name = "prod"
# while for
index = 0
while index < len(my_name):
    print(my_name[index], "\t", end='')
    index += 1
print()
for n in my_name:
    print(n + "\t", end='')
print()

"""
给定一个字符串："itheima itcast boxuegu"
统计字符串内有多少个"it"字符
将字符串内的空格，全部替换为字符："|"
并按照"|"进行字符串分割，得到列表  
"""

name = "itheima itcast boxuegu"
print(f"统计字符串内有多少个'it'字符{name.count('it')}")
new_name = name.replace(" ", "|")
print(f"将字符串内的空格，全部替换为字符：'|' -> {new_name}")
my_name_array = new_name.split("|")
print(f"my_name_array - > {my_name_array}")
