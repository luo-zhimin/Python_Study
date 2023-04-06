# 地图可视化

# 导包
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
my_map = Map()
# 准备数据
data = [
    # todo !!!注意要和地图名字一一对应
    ("上海市", 99),
    ("北京市", 199),
    ("台湾省", 299),
    ("湖南省", 399),
    ("河南省", 499)
]
# 添加对象
my_map.add("地图", data, 'china')

# 添加全局属性
my_map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
            {"min": 100, "max": 499, "label": "100-449人", "color": "#FF6666"},
        ]
    )
)

# 生成对象
my_map.render("my_map.html")
