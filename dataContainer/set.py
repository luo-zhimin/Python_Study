"""
    集合，最主要的特点就是：不支持元素的重复（自带去重功能）、并且内容无序
    集合使用：{}
    因为集合是无序的，所以集合不支持：下标索引访问

"""

# 集合的常用操作
# 定义
my_set = {'prod', 'test', 'nerve', 'happy', 'order', 'prod', 'order'}
print(f"my_set的内容是{my_set},类型是{type(my_set)}")
# 添加 add
my_set.add('Python')
print(f"my_set add -> {my_set}")
# 移除
my_set.remove('test')
print(f"remove test -> {my_set}")
# pop 随机取出一个元素 并且移除
p = my_set.pop()
print(f"my_set pop -> {p} 还有{my_set}")
# 清空
# my_set.clear()

# 取2个集合差集
# 得到新的集合 老的不变
set1 = {1, 2, 3}
set2 = {2, 4, 5}
# 表示 1里面没有2的差集 4，5
# 语法：集合1.difference(集合2)，功能：取出集合1和集合2的差集（集合1有而集合2没有的）
set3 = set2.difference(set1)
print(f"set2 difference set1 -> {set3}")
# 消除2个集合差集
# 集合1.difference_update(集合2)
# 对比集合1和集合2，在集合1内，删除和集合2相同的元素
# 结果：集合1被修改，集合2不变
set1.difference_update(set2)
print(f"difference_update - > set1 {set1}")
print(f"difference_update - > set2 {set2}")
# 合并
set3 = set2.union(set1)
print(f"set1 union set2 ->{set3}")
# 统计集合的数量
len(set1)

# 遍历
# 不支持下标 所以没有while循环 只有for循环
for s in set3:
    print(s, "\t", end='')
print()
"""
有如下列表对象：
    my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
    
    请：
    定义一个空集合
    通过for循环遍历列表
    在for循环中将列表的元素添加至集合
    最终得到元素去重后的集合对象，并打印输出
"""

my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
set4 = set()
for m in my_list:
    set4.add(m)

print(f"exercise result -> {set4}")
