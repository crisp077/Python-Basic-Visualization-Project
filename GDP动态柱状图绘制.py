"""
    GDP动态柱状图绘制
"""

from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取数据
f = open("可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除第一行
data_lines.pop(0)
# 将数据转换为字典存储，格式为：
# { 年份: [ [国家, GDP], [国家, GDP], ... ], 年份: [ [国家, GDP], [国家, GDP], ... ], ... }
# 定义一个字典对象
data_dict = {}  # 空字典
for line in data_lines:
    year = int(line.split(",")[0])  # 年份
    country = line.split(",")[1]  # 国家
    gdp = float(line.split(",")[2])  # GDP
    # 如何判断字典里面有没有指定的key?
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 创建时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})

# 排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年份前20的国家
    year_data = data_dict[year][0:20]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])  # x轴添加国家
        y_data.append(country_gdp[1] / 100000000)  # y轴添加gdp

    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("DGP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转x轴和y轴
    bar.reversal_axis()
    # 设置每一年图标的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前20GDP数据")
    )

    timeline.add(bar, str(year))

# 设置时间线自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
# 绘图
timeline.render("1960-2019全球GDP前20国家.html")
