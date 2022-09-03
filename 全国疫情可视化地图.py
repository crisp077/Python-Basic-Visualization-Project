"""
    演示全国疫情可视化地图开发
"""

import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取数据文件
f = open("可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()  # 全部数据
# 关闭文件
f.close()
# 取到各省数据
# 将json转换为python字典
data_dict = json.loads(data)  # 基础数据字典
# 从字典中取出省份数据
province_data_list = data_dict["areaTree"][0]["children"]
# 组装每个省份和确诊人数为元组，并将各个省的数据都封装入列表内
data_list = []  # 绘图需要用的数据
for province_data in province_data_list:
    province_name = province_data["name"]  # 省份名称
    province_total_confirm = province_data["total"]["confirm"]  # 确诊人数
    data_list.append((province_name, province_total_confirm))

# 创建地图对象
map = Map()
# 添加数据
map.add("各省份确诊人数", data_list, "china")
# 设置全局配置
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 99, "label": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 499, "label": "100~499人", "color": "#FFFF99"},
            {"min": 500, "max": 999, "label": "500~999人", "color": "#FF9966"},
            {"min": 1000, "max": 1999, "label": "1000~1999人", "color": "#FF6666"},
            {"min": 2000, "max": 3999, "label": "2000~3999人", "color": "#CC3333"},
            {"min": 4000, "label": "4000以上", "color": "#990033"},
        ]
    )
)
# 绘图
map.render("全国疫情地图.html")
