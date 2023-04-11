"""
    first exercise
"""
import json
import os

from pyspark import SparkConf, SparkContext

os.environ['PYSPACK_PYTHON'] = '/usr/bin/python3'

conf = SparkConf().setMaster('local[*]').setAppName('readFile')
sc = SparkContext(conf=conf)
# file = sc.textFile("hello.txt")
# word_rdd = file.flatMap(lambda a: a.split(" "))
# # print(word_rdd.collect())
# # 转换为2元元祖
# word_two_tuple = word_rdd.map(lambda word: (word, 1))
# # print(word_two_tuple.collect())
# # group by sum
# result = word_two_tuple.reduceByKey(lambda x, y: x + y)
# # print(f"result = {result.collect()}")
# # sortBy ascending=True sort /ascending=False reserve
# sort_result = result.sortBy(lambda a: a[1], ascending=False, numPartitions=1)
# print(sort_result.collect())

# second exercise
file_rdd = sc.textFile("orders.txt")
all_file_rdd = file_rdd.flatMap(lambda f: f.split("|"))
# print(all_file_rdd.collect())
# group by sort
# transform dict
dict_rdd = all_file_rdd.map(lambda x: json.loads(x))
# print(dict_rdd.collect())
area_tuple = dict_rdd.map(lambda x: (x['areaName'], int(x['money'])))
# print(area_tuple.collect())
# 城市销售额度 从大到小 排序
area_tuple2 = area_tuple.reduceByKey(lambda x, y: x + y)
# sort  [('北京', 91556), ('杭州', 28831), ('天津', 12260), ('上海', 1513), ('郑州', 1120)]
area_sort = area_tuple2.sortBy(lambda element: element[1], ascending=False, numPartitions=1)
print(f"需求1: {area_sort.collect()}")

# 二 全部城市 那些商品在售卖
category_tuple = dict_rdd.map(lambda x: (x['areaName'], x['category']))
categories = category_tuple.map(lambda x: x[1]).distinct()
print(f"需求2: {categories.collect()}")

# 北京 售卖 商品
beiJi = category_tuple.filter(lambda x: x[0] == '北京').map(lambda y: y[1]).distinct()
print(f"需求3: {beiJi.collect()}")

# print(area_sort.collect())
sc.stop()
