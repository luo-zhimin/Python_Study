# 国内疫情地图
import json

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts


def province(name):
    provinces = ["北京市", "天津市", "河北省", "山西省", "内蒙古自治区", "辽宁省", "吉林省", "黑龙江省", "上海市",
                 "江苏省", "浙江省", "安徽省", "福建省", "江西省",
                 "山东省", "河南省", "湖北省", "湖南省", "广东省", "广西壮族自治区", "海南省", "重庆市", "四川省",
                 "贵州省", "云南省", "西藏自治区", "陕西省", "甘肃省",
                 "青海省", "宁夏回族自治区", "新疆维吾尔自治区", "台湾省", "香港特别行政区", "澳门特别行政区"]
    for pro in provinces:
        if pro.__contains__(name):
            return pro
        else:
            continue


# 读取文件
f = open('/Users/luozhimin/Desktop/Project/Python_Study/data/可视化案例数据/地图数据/疫情.txt', 'r', encoding="utf-8")
# 全部数据读取
data = f.read()
f.close()

# 字符串转换字典
data_dict = json.loads(data)
# 取出省份的元素
province_data_list = data_dict['areaTree'][0]['children']
# 数据组装 元组 for
result_data = []
for province_data in province_data_list:
    # 名称
    province_name = province_data['name']
    province_name = province(province_name)
    # 确定人数
    province_confirm = province_data['total']['confirm']
    result_data.append((province_name, province_confirm))

# 地图构建
country_map = Map()
country_map.add("各省份确诊人数", result_data, 'china')
country_map.set_global_opts(
    # 分段视觉映射
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000+人", "color": "#990033"},
        ]
    ),
    title_opts=TitleOpts(title="全国疫情地图")
)
country_map.render('全国疫情地图.html')
print(result_data)
