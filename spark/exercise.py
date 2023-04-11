"""
    first exercise
"""
import os

from pyspark import SparkConf, SparkContext

os.environ['PYSPACK_PYTHON'] = '/usr/bin/python3'

conf = SparkConf().setMaster('local[*]').setAppName('readFile')
sc = SparkContext(conf=conf)
file = sc.textFile("hello.txt")
word_rdd = file.flatMap(lambda a: a.split(" "))
print(word_rdd.collect())
# 转换为2元元祖
word_two_tuple = word_rdd.map(lambda word: (word, 1))
print(word_two_tuple.collect())
# group by sum
result = word_two_tuple.reduceByKey(lambda x, y: x + y)
print(f"result = {result.collect()}")
sc.stop()
