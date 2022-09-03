"""
    演示湖北省疫情地图开发
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
# 从字典中取出湖北省各地区数据
area_data_list = data_dict["areaTree"][0]["children"][6]["children"]
# 组装每个地区和确诊人数为元组，并将各地区的数据都封装入列表内
data_list = []  # 绘图需要用的数据
for area_data in area_data_list:
    area_name = area_data["name"]  # 省份名称
    area_name += "市"
    area_total_confirm = area_data["total"]["confirm"]  # 确诊人数
    data_list.append((area_name, area_total_confirm))

# 创建地图对象
map = Map()
# 添加数据
map.add("湖北省各地区确诊人数", data_list, "湖北")
# 设置全局配置
map.set_global_opts(
    title_opts=TitleOpts(title="湖北省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 49, "label": "1~19人", "color": "#CCFFFF"},
            {"min": 50, "max": 99, "label": "20~49人", "color": "#FFFF99"},
            {"min": 100, "max": 499, "label": "50~99人", "color": "#FF9966"},
            {"min": 500, "max": 999, "label": "100~499人", "color": "#FF6666"},
            {"min": 1000, "max": 4999, "label": "500~999人", "color": "#CC3333"},
            {"min": 4999, "label": "4999以上", "color": "#990033"},
        ]
    )
)
# 绘图
map.render("湖北省疫情地图.html")