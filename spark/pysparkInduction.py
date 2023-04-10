"""
    spark induction
"""
# 导包
from pyspark import SparkConf, SparkContext

# 创建SparkConf对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基于SparkConf创建SparkContext对象
sc = SparkContext(conf=conf)

# 运行版本
print(sc.version)

# 停止
sc.stop()
