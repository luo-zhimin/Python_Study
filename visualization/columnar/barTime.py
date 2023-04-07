"""
    base timeLine
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import *
from pyecharts.options import *

# 构建基础时间线图
bar1 = Bar()
# x
bar1.add_xaxis(["中国", "英国", "美国"])
# y
bar1.add_yaxis("GDP", [10, 20, 30], label_opts=LabelOpts(position="right"))  # 位置放到右面 position
# 反转xy轴
bar1.reversal_axis()

bar2 = Bar()
# x
bar2.add_xaxis(["中国", "英国", "美国"])
# y
bar2.add_yaxis("GDP", [50, 100, 150], label_opts=LabelOpts(position="right"))  # 位置放到右面 position
# 反转xy轴
bar2.reversal_axis()

bar3 = Bar()
# x
bar3.add_xaxis(["中国", "英国", "美国"])
# y
bar3.add_yaxis("GDP", [100, 200, 300], label_opts=LabelOpts(position="right"))  # 位置放到右面 position
# 反转xy轴
bar3.reversal_axis()

# 构建时间线对象
# 设置主题
timeline = Timeline({"theme": ThemeType.LIGHT})

timeline.add(bar1, "点1")
timeline.add(bar2, "点2")
timeline.add(bar3, "点3")

# 自动播放设置
timeline.add_schema(
    # 间隔时间-毫秒
    play_interval=1000,
    # 是否显示时间线
    is_timeline_show=True,
    # 是否自动播放
    is_auto_play=True,
    # 是否循环播放
    is_loop_play=True
)

# 绘图 时间线绘图 不是bar对象
timeline.render("基础时间线绘图.html")
