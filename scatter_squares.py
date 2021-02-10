'''
* @Author: csy 
* @Date: 2019-05-15 21:40:25 
* @Last Modified by:   csy 
* @Last Modified time: 2019-05-15 21:40:25 
'''
import matplotlib.pyplot as plt
x_values = list(range(1, 1001))  # 定义x
y_values = [x**2 for x in x_values]  # 定义y
# plt.scatter(x_values,y_values,c='red',edgecolors='none',s=40)
# plt.scatter(x_values,y_values,c=(1,0,0),edgecolors='none',s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolors='none', s=40)  # 颜色映射
plt.title("Square Numbers", fontsize=24)  # 设置标题
plt.xlabel("Value", fontsize=14)  # 设置横坐标标签
plt.ylabel("Square of Value", fontsize=14)  # 设置纵坐标标 签
plt.tick_params(axis='both', which='major', labelsize=14)  # 设置刻度标记的大小
plt.axis([0, 1100, 0, 1100000])  # 修改坐标轴取值范围
plt.savefig("squares_plot.png", bbox_inches='tight')  # 保存图片
plt.show()  # 显示图表
