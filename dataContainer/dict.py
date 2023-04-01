"""
 dict => Java Map<Key,Value>
 字典的定义，同样使用{}，不过存储的元素是一个个的：键值对，如下语法
 {key:value,key:value}
    使用{}存储原始，每一个元素是一个键值对
    每一个键值对包含Key和Value（用冒号分隔）
    键值对之间使用逗号分隔
    Key和Value可以是任意类型的数据（key不可为字典）
    Key不可重复，重复会对原有数据覆盖

    空字典
    {} dict()

    字典获取
        字典同集合一样，不可以使用下标索引
        但是字典可以通过Key值来取得对应的Value

    字典的Key和Value可以是任意数据类型（Key不可为字典）
"""
import random

# 定义字典
dict1 = {"王力宏": 99, "赵丽颖": 88, "刘亦菲": 99}
# 定义空的字典
d = {}
d2 = dict()
# 定义重复key
dict2 = {"王力宏": 99, "赵丽颖": 88, "刘亦菲": 99, "刘亦菲": 100}
print(f"重复定义key字典->{dict2}")
# 字典获取
# 字典同集合一样，不可以使用下标索引
# 但是字典可以通过Key值来取得对应的Value
score = dict2['刘亦菲']
print(f"刘亦菲的考试分数是{score}")
# 嵌套字典
# 学生成绩
score_dict = {
    "王力宏": {"语文": 77, "数学": 66, "英语": 33},
    "周杰伦": {"语文": 88, "数学": 86, "英语": 55},
    "林俊杰": {"语文": 99, "数学": 96, "英语": 66},
}
print(f"score_dict -> {score_dict}")
# 从嵌套字典里面获取数据
# 看一下周杰伦的语文成绩
zhou_chinese = score_dict["周杰伦"]["语文"]
print(f"周杰伦的语文成绩{zhou_chinese}")

# 常用操作
# 新增
dict2["胡歌"] = 100
print(f"dict add result = {dict2}")
# 修改
dict2["王力宏"] = 82
print(f"dict update result = {dict2}")
# 删除
p = dict2.pop("王力宏")
print(f"dict pop element = {p} result = {dict2}")
# 清空
# dict2.clear()
# 获取全部key
dict2_keys = dict2.keys()
print(f"dict2_keys = {dict2_keys}")
# 获取全部value
dict2_values = dict2.values()
print(f"dict2_values = {dict2_values}")
# 遍历
for key in dict2.keys():
    print(f"学生{key},成绩为{dict2[key]}")
# 长度 计算字典内的全部元素（键值对）数量
print(f"dict2 len = {len(dict2)}")
# 特点

# exercise
employ = {"王力宏": {"部门": "科技部", "工资": 3000, "级别": 1},
          "周杰伦": {"部门": "市场部", "工资": 5000, "级别": 2},
          "林俊杰": {"部门": "市场部", "工资": 7000, "级别": 3},
          "张学友": {"部门": "科技部", "工资": 4000, "级别": 1},
          "刘德华": {"部门": "市场部", "工资": 6000, "级别": 2},
          }

print(f"全体员工信息:\n{employ}")

for element in employ:
    if employ[element]["级别"] == 1:
        employ[element]["级别"] += 1
        employ[element]["工资"] += 1000

print(f"加薪之后\n{employ}")

# len
print(f"列表长度为{len([1, 2, 34, 5, 7])}")
# max
print(f"列表最大的数为{max([1, 2, 34, 5, 7])}")
# min
print(f"列表最小的数为{min([1, 2, 34, 5, 7])}")

# 类型转换
print(f"转换->{list(dict2)}")

# sort -> list
num_str = "1298653"
print(f"sort->{sorted(num_str, reverse=True)}")

# exercise
# 幸运数字6
number = int(input("请输入您的幸运数字(1-8): "))
nums = []
lucky = []
i = 1
while i <= number:
    if i % 6 == 0:
        lucky.append(i)
    nums.append(i)
    i += 1
print(f"nums={nums}")
print(f"lucky={lucky}")
# 嵌套
rooms = [[], [], []]
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
i, sourceIndex = 0, len(teachers)
# random
teachers = set(teachers)
# print(len(rooms))
# print(rooms[0])
while i < sourceIndex:
    roomId = random.randint(0, 2)
    print(f"我是第{roomId}个教室")
    teacher = teachers.pop()
    rooms[roomId].append(teacher)
    print(f"this current teacher {teacher}")
    i += 1
print(f"result -> {rooms}")
