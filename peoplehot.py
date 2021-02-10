'''
* @File: peoplehot.py
* @Author: CSY
* @Date: 2019/7/21 - 22:45
'''
import numpy as np
import pandas as pd
import folium
import webbrowser
from folium.plugins import HeatMap
# posi=pd.read_csv("D:\\Files\\datasets\\CitiesLatLon_China.csv")

posi=pd.read_excel(r".\2017年度城市GDP人口排名.xls")

num = 100

lat = np.array(posi["LAT"][0:num])                        # 获取维度之维度值
lon = np.array(posi["LON"][0:num])                        # 获取经度值
pop = np.array(posi["POP"][0:num],dtype=float)    # 获取人口数，转化为numpy浮点型
gdp = np.array(posi["GDP"][0:num],dtype=float)    # 获取GDP数，转化为numpy浮点型
gdp_average = np.array(posi["GDP_Average"][0:num],dtype=float) # 获取人均GDP数，转化为numpy浮点型

data = [[lat[i],lon[i],gdp_average[i]] for i in range(num)]    #将数据制作成[lats,lons,weights]的形式

map_osm = folium.Map(location=[35,110],zoom_start=6)    #绘制Map，开始缩放程度是5倍
HeatMap(data).add_to(map_osm)  # 将热力图添加到前面建立的map里

file_path = r".\城市GDP地图可视化.html"
map_osm.save(file_path)     # 保存为html文件

webbrowser.open(file_path)  # 默认浏览器打开