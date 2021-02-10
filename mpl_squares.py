'''
* @Author: csy 
* @Date: 2019-05-15 20:25:45 
* @Last Modified by:   csy 
* @Last Modified time: 2019-05-15 20:25:45 
'''
import matplotlib.pyplot as plt
input_values=[1,2,3,4,5]#定义值
squares=[1,4,9,16,25]#定义平方值
plt.plot(input_values,squares,linewidth=5)#描绘点并定义线条宽度为5
plt.title("Square Numbers",fontsize=24)#设置标题
plt.xlabel("Value",fontsize=14)#设置横坐标标签
plt.ylabel("Square of Value",fontsize=14)#设置纵坐标标签
plt.tick_params(axis='both',labelsize=14)#设置刻度标记的大小
plt.show()#显示图表