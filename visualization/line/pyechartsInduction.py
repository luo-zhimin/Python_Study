"""
    全局配置选项可以通过set_global_opts方法来进行配置
"""
# 导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 得到折线图对象
line = Line()
# x轴
line.add_xaxis(['英国', '美国', '中国'])
# y
line.add_yaxis('GDP', [30, 20, 10])
# 设置global属性 全局属性
line.set_global_opts(
    title_opts=TitleOpts(title='GDP展示', pos_left='center', pos_bottom='1%'),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

# render
line.render()
