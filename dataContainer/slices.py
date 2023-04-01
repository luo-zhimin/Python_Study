"""
    序列是指：内容连续、有序，可使用下标索引的一类数据容器
    列表、元组、字符串，均可以可以视为序列

    序列支持切片，即：列表、元组、字符串，均支持进行切片操作

    切片：从一个序列中，取出一个子序列
    语法：序列[起始下标:结束下标:步长]
    表示从序列中，从指定位置开始，依次取出元素，到指定位置结束，得到一个新序列：

        起始下标表示从何处开始，可以留空，留空视作从头开始
        结束下标（不含）表示何处结束，可以留空，留空视作截取到结尾
        步长表示，依次取元素的间隔
            步长1表示，一个个取元素
            步长2表示，每次跳过1个元素取
            步长N表示，每次跳过N-1个元素取
            步长为负数表示，反向取（注意，起始下标和结束下标也要反向标记）
    注意，此操作不会影响序列本身，而是会得到一个新的序列（列表、元组、字符串）
"""
# 对list进行切片
my_list = [0, 1, 2, 3, 4, 5, 6, 7]
slices_list = my_list[1:4]  # step 默认是1 所以可以省略不写
print(f"结果1：{slices_list}")

# 对tuple进行切片 从头结束到尾结束 step=1
my_tuple = (1, 2, 3, 4, 5)
# 起始-结束不写表示从头到尾  step default 1
slices_tuple = my_tuple[:]
print(f"结果2：{slices_tuple}")
# 对str进行切片 step为2
my_str = "12345678"
slices_str = my_str[::2]
print(f"结果3：{slices_str}")

# reserve list tuple str (number need reserve too)
print(f"结果4：{my_list[::-1]}")
print(f"结果5：{my_tuple[3:0:-1]}")
print(f"结果6：{my_str[8:0:-2]}")

"""
有字符串："万过薪月，员序程马黑来，nohtyP学"
请使用学过的任何方式，得到 黑马程序员
"""
name = "万过薪月，员序程马黑来，nohtyP学"
print(f"reserve -> {name[::-1]}")
name_array = name.split("，")
new_name = name_array[1]
result = new_name.replace('来', '')
print(f"result - > {result[::-1]}")
