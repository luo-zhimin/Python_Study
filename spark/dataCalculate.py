"""
    map
        map算子，是将RDD的数据一条条处理（处理的逻辑基于map算子中接收的处理函数），返回新的RDD
    flatMap
        功能：对rdd执行map操作，然后进行解除嵌套操作.
    reduceByKey
        group by 进行value运算
    filter
        过滤出true的数据
    distinct
        set
    sortBy

"""
import os

from pyspark import SparkConf, SparkContext

# 设置环境变量
os.environ['PYSPACK_PYTHON'] = '/usr/bin/python3'

# 创建spark对象
conf = SparkConf().setMaster('local[*]').setAppName('my_spark_app')
sc = SparkContext(conf=conf)

# 准备一个rdd
# rdd = sc.parallelize([1, 2, 3, 45, 6])

# calculate
# (T)->U
# outer function
# def func(data):
#     return data * 10

# inner function chain
# rdd_map = rdd.map(lambda element: element * 10).map(lambda element: element + 5)

# print(rdd_map.collect())

# flatMap
# rdd = sc.parallelize(["itheima itcase 666", "itheima itheima itcase", "python itheima"])
# flatMap 解除嵌套 多个list嵌套
# rdd2 = rdd.flatMap(lambda s: s.split(" "))
# print(rdd2.collect())

# reduceByKey group by key handle value
# rdd = sc.parallelize([("男", 99), ("女", 88), ("女", 99), ("男", 66)])
# rdd2 = rdd.reduceByKey(lambda a, b: a + b)
# print(rdd2.collect())

# filter
# rdd = sc.parallelize([1, 2, 3, 4, 5])
# rdd2 = rdd.filter(lambda a: a % 2 == 0)
# print(rdd2.collect())

# distinct
# rdd = sc.parallelize([1, 2, 3, 4, 3, 2, 5, 7, 1])
# rdd2 = rdd.distinct()
# print(rdd2.collect())  # [1, 2, 3, 4, 5, 7]


# stop
sc.stop()
