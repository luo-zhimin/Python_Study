"""
    只读
    元组同列表一样，都是可以封装多个、不同类型的元素在内。
    但最大的不同点在于：
    元组一旦定义完成，就不可修改
    所以，当我们需要在程序内封装数据，又不希望封装的数据被篡改，那么元组就非常合适了

    元组定义：定义元组使用小括号，且使用逗号隔开各个数据，数据可以是不同的数据类型
    元组只有一个数据，这个数据后面要添加逗号

    元组由于不可修改的特性，所以其操作方法非常少
    特点
        元组由于不可修改的特性，所以其操作方法非常少
        可以修改元组内的list的内容（修改元素、增加、删除、反转等
        不可以替换list为其它list或其它类型
"""
# 定义元组
t1 = ('1', '2', True)
t2 = tuple()
# todo 元组只有一个数据，这个数据后面要添加逗号
t3 = ('hello',)

print(f"t1 type {type(t1)},result -> {t1}")
print(f"t2 type {type(t2)},result -> {t2}")
print(f"t3 type {type(t3)},result -> {t3}")

t4 = ((1, 2, 3), (4, 5, 6), (6, 7, 8))
print(t4)
# 通过下标索引取值
print(t4[1][2])  # 6

# index count len

# 多重数组不可以这种取值
# i = t4.index(4)

i = t1.index('1')
print(f"在t1里面4的下标是{i}")

count = t4.count(6)
print(f"在t4中6的个数是{count}个")

print(f"t4的长度为{len(t4)}")

# 循环
# tuple while foreach
index = 0
# 单循环 单成
# while index < len(t1):
while index < len(t4):
    # 再次遍历
    s_index = 0
    while s_index < len(t4[index]):
        print(t4[index][s_index], "\t", end='')
        s_index += 1
    # print(t4[index])
    index += 1
print("\ntuple while finish")

# for
for x in t1:
    print(x, "\t", end='')
print()
# 元组由于不可修改的特性，所以其操作方法非常少

# 不可以修改元组的内容，否则会直接报错
t6 = (1, 2, ['Java', 'Python', 'Kafka'])
# 'tuple' object does not support item assignment
# t6[1] = 6
# 可以修改元组内的list的内容（修改元素、增加、删除、反转等）
t6[2][2] = 'RabbitMq'
print(f"修改后tuple result ->{t6}")
# 不可以替换list为其它list或其它类型
# error
# t6[1] = ['Spring']

# exercise
"""
定义一个元组，内容是：（'周杰轮', 11, ['football', 'music']），
记录的是一个学生的信息（姓名、年龄、爱好）

请通过元组的功能（方法），对其进行
查询其年龄所在的下标位置
查询学生的姓名
删除学生爱好中的football
增加爱好：coding到爱好list内
"""
star = ('周杰轮', 11, ['football', 'music'])
age = star.index(11)
print(f"年龄所在的下标位置{age}")
# 查询学生的姓名
name = star.index('周杰轮')
print(f"查询学生的姓名{name}")
# 删除学生爱好中的football
star[2][0] = ''
print(f"删除学生爱好中的football result -> {star}")
# 增加爱好：coding到爱好list内
star[2][1] = 'coding'
print(f"增加爱好 result -> {star}")
