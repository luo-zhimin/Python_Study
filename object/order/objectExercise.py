# 1月份数据是普通文本，使用逗号分割数据记录，从前到后分别是（日期，订单id，销售额，销售省份）

# from data_define import Order
from pyecharts.charts import Bar
from pyecharts.globals import *
from pyecharts.options import *

from file_define import TextFileReader, JsonFileReader

reader = TextFileReader("/Users/luozhimin/Desktop/Project/Python_Study/data/面向对象/2011年1月销售数据.txt")
texts = reader.read_data()
json_reader = JsonFileReader(
    '/Users/luozhimin/Desktop/Project/Python_Study/data/面向对象/2011年2月销售数据JSON.txt')
jsons = json_reader.read_data()

# 将俩个月的数据合并
all_orders = texts + jsons
# for o in all_orders:
#     print(o)
# 数据计算
order_dict = {}
for order in all_orders:
    if order.date in order_dict.keys():
        order_dict[order.date] += order.money
    else:
        order_dict[order.date] = order.money

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(order_dict.keys()))
bar.add_yaxis("销售额", list(order_dict.values()), label_opts=LabelOpts(is_show=False))

bar.set_global_opts(
    title_opts=TitleOpts(title="销售额"),
)

bar.render("每日销售额.html")
print(order_dict)
