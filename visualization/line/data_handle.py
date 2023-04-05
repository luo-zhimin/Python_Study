# 导入模块
import json

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts, AxisOpts

directory = '/Users/luozhimin/Desktop/Project/Python_Study/data/可视化案例数据/折线图数据'
# 处理数据
# 美国全部数据
f_us = open(directory + "/美国.txt", 'r',
            encoding='UTF-8')
us_data = f_us.read()

# 日本全部数据
f_jp = open(directory + "/日本.txt", 'r',
            encoding='UTF-8')
jp_data = f_jp.read()

# 印度全部数据
f_in = open(directory + "/印度.txt", 'r',
            encoding='UTF-8')
in_data = f_in.read()

# 去掉开头
us_data = us_data.replace('jsonp_1629344292311_69436(', '')
jp_data = jp_data.replace('jsonp_1629350871167_29498(', '')
in_data = in_data.replace('jsonp_1629350745930_63180(', '')

# 去掉结尾 不包含
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# 将json转换为字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# get key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# date 只取一年 2020年
ux_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# person count 取出确诊
ux_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 构建图表
line = Line()
# x common use once country
line.add_xaxis(ux_x_data)
# y
# 设置系列属性
line.add_yaxis('美国确诊人数', ux_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis('日本确诊人数', jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis('印度确诊人数', in_y_data, label_opts=LabelOpts(is_show=False))

# 设置全局选项
line.set_global_opts(
    title_opts=TitleOpts(title='2020年美日印三国确诊折线图', pos_left='center', pos_bottom='1%'),
    yaxis_opts=AxisOpts(name='确诊人数'),
    xaxis_opts=AxisOpts(name='时间')
)

# 生成图表
line.render()

# 关闭文件
f_us.close()
f_jp.close()
f_in.close()
