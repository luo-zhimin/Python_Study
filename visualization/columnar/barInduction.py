"""
    bar Induction
"""
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()
# x
bar.add_xaxis(["中国", "英国", "美国"])
# y
bar.add_yaxis("GDP", [10, 20, 30], label_opts=LabelOpts(position="right"))  # 位置放到右面 position
# 反转xy轴
bar.reversal_axis()

bar.render("bar.html")
