import json

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

# 读取文件
f = open('/Users/luozhimin/Desktop/Project/Python_Study/data/可视化案例数据/地图数据/疫情.txt', 'r', encoding="utf-8")
# 全部数据读取
data = f.read()
f.close()

# 转换
data_dict = json.loads(data)
# 找到全部省份的数据
all_provinces_list = data_dict['areaTree'][0]['children']
# 找到对应省份的数据 for也可以 if
province_data_list = all_provinces_list[3]['children']

result_data = []
for province_data in province_data_list:
    province_name = province_data['name'] + '市'
    # 特殊处理
    if province_name == '济源示范区市':
        province_name = '济源市'
    province_confirm = province_data['total']['confirm']
    result_data.append((province_name, province_confirm))

province_map = Map()
province_map.add("河南省疫情地图", result_data, '河南')
province_map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 10, "label": "1-10人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FF9966"},
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF6666"},
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#CC3333"},
            {"min": 10000, "label": "10000+人", "color": "#990033"},
        ]
    )
)

province_map.render("河南省疫情地图.html")

print(result_data)
