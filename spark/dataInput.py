# 数据输入
from pyspark import SparkConf, SparkContext

# 创建spark对象
conf = SparkConf().setMaster('local[*]').setAppName('my_spark_app')
sc = SparkContext(conf=conf)
# 加载 parallelize RDD
# rdd_list = sc.parallelize([1, 23, 4])
# rdd_tuple = sc.parallelize((1, 23, 4))
# rdd_set = sc.parallelize({1, 3, 4, 5})
# rdd_dict = sc.parallelize({"key": "value", "key1": "value1"})
# rdd_str = sc.parallelize('123')
#
# # 如果要查看rdd里面的内容需要用 collect
# print(rdd_list.collect())
# print(rdd_tuple.collect())
# print(rdd_set.collect())
# print(rdd_dict.collect())
# print(rdd_str.collect())

rdd = sc.textFile(name="hello.txt")
print(rdd.collect())
sc.stop()
