"""
    动态GDP图绘画
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import *
from pyecharts.options import *

# 1. 掌握列表的sort方法并配合lambda匿名函数完成列表排序
# my_list = [['a', 33], ['b', 55], ['c', 11]]

# 排序 基于带名函数
# def choose_sort_key(element):
#     return element[1]
# my_list.sort(key=choose_sort_key, reverse=True)

# lambda
# my_list.sort(key=lambda element: element[1], reverse=True)
#
# print(f"sort {my_list}")

# 2. 完成图表所需的数据处理
f = open("/Users/luozhimin/Desktop/Project/Python_Study/data/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv",
         "r", encoding='GB2312')
# year,GDP,rate
lines = f.readlines()
f.close()
# 去除标头
lines.pop(0)
# print(lines)

# 转换为字典 {"year":[[country,gdp],[]]}
# 先定义一个字典对象
data_dict = {}
for line in lines:
    # 1960,美国,5.43E+11
    line_data = line.strip().split(",")
    year = int(line_data[0])
    country = line_data[1]
    # 有科学计数法
    gdp = float(line_data[2])

    try:
        # has
        data_dict[year].append([country, gdp])
    except KeyError as e:
        # no has need a new dict init list add assignment
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 3. 完成GDP动态图表绘制
# 年份排序
sorted_year = sorted(data_dict.keys())
# print(f"sorted_year {sorted_year}")

#   创建时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})

for year in sorted_year:
    # 取当前年对应的list
    # big -> small
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 构建bar 取全球前8
    gdp_year_list = data_dict[year][0:8]
    # country
    x_data = []
    # gdp
    y_data = []
    for country_gdp in gdp_year_list:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1] / 100000000)

    # 构建Bar
    bar = Bar()
    # 反转从大到小
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis('GDP(亿)', y_data, label_opts=LabelOpts(position="right"))
    # 反转
    bar.reversal_axis()
    # 设置每一年的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    timeline.add(bar, str(year))

# 设置属性
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
# 绘图
timeline.render("1960-2019年全球gdp前8国家.html")
