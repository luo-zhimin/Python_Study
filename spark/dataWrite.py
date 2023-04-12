"""
    数据输出
"""
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("app")
# 设置分区 parallelism
# conf.set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)
# ParallelCollectionRDD
rdd = sc.parallelize([1, 1, 3, 4, 5, 6, 7], numSlices=1)
# 输出list对象
# rdd_list: list = rdd.collect()
# print(f"list:{rdd_list}")
# # reduce 聚合
# rdd_reduce = rdd.reduce(lambda a, b: a + b)
# print(f"reduce:{rdd_reduce}")
# # take() 取前多少个数据
# rdd_take = rdd.take(3)
# print(f"take:{rdd_take}")
# # count
# rdd_count = rdd.count()
# print(f"count:{rdd_count}")

# 输出到文件中
# 需要配置hadoop 我是os暂时不需要
rdd.saveAsTextFile("test.txt")

sc.stop()
