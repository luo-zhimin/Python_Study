"""
    first exercise
"""
import json
import os

from pyspark import SparkConf, SparkContext

os.environ['PYSPACK_PYTHON'] = '/usr/bin/python3'

conf = SparkConf().setMaster('local[*]').setAppName('readFile')
conf.set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)
file = sc.textFile("hello.txt")
word_rdd = file.flatMap(lambda a: a.split(" "))
# print(word_rdd.collect())
# 转换为2元元祖
word_two_tuple = word_rdd.map(lambda word: (word, 1))
# print(word_two_tuple.collect())
# group by sum
result = word_two_tuple.reduceByKey(lambda x, y: x + y)
# print(f"result = {result.collect()}")
# sortBy ascending=True sort /ascending=False reserve
sort_result = result.sortBy(lambda a: a[1], ascending=False, numPartitions=1)
print(sort_result.collect())
print("first exercise")
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

print("last exercise")
search_data = sc.textFile("search_log.txt").map(lambda search: search.split("\t"))
# print(search_data.take(3))
# 转换为二元元祖 时间 map<time,count>
time_tuple = search_data.map(lambda a: (a[0][:2], 1))
# print(time_tuple.collect())
# 分组 聚合
time_group_count = time_tuple.reduceByKey(lambda a, b: a + b)
# print(time_group_count.collect())
# sort
time_sort_take = time_group_count.sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(3)
print(f"热门搜索时间段Top3:{time_sort_take}")

# 热门搜索词语 top3
# 组装
word_tuple = search_data.map(lambda a: (a[2], 1))
# print(word_tuple.collect())
# 分组 排序 取前三
word_group_sort_take = word_tuple.reduceByKey(lambda a, b: a + b). \
    sortBy(lambda a: a[1], ascending=False,
           numPartitions=1).take(3)
print(f"热门搜索词语 top3 :{word_group_sort_take}")

# 黑马程序员关键字 时间搜索最多 (time,word)
# 找到所有的符合条件的值
word_time_filter_tuple = search_data.filter(lambda a: a[2] == '黑马程序员'). \
    map(lambda a: (a[0][:2], 1))
# print(word_time_filter_tuple.collect())
# 进行聚合 取top1
word_group_reduce_sort_take = word_time_filter_tuple.reduceByKey(lambda a, b: a + b). \
    sortBy(lambda a: a[1],
           ascending=False,
           numPartitions=1).take(1)
print(f"黑马程序员关键字 时间搜索最多 top1 :{word_group_reduce_sort_take}")

# 将数据转换为json 并且写出文件
# 是否组装对象 或者 新的dict ？
search_dict = search_data.map(
    lambda a: {"time": a[0], "user_id": a[1], "keywords": a[2], "search_sort": a[3], "click": a[4], "url": a[5]})
# print(search_dict.collect())
# write
search_dict.saveAsTextFile("search.json")
sc.stop()
