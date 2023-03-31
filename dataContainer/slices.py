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