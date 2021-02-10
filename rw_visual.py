import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 不断模拟随机漫步
while True:
    # 创建实例
    rw = RandomWalk(50000)#实例化类
    rw.fill_walk()#调用方法
    point_numbers = list(range(rw.num_points))#定义数组
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolor='none', s=1)#通过渐变色显示漫步数
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)#突出显示起点，绿色
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)#突出显示终点，红色
    plt.axes().get_xaxis().set_visible(False)#隐藏X轴
    plt.axes().get_yaxis().set_visible(False)#隐藏Y轴
    plt.figure(dpi=128, figsize=(10, 6))#绘制一个10*6英寸，每英寸长度内的像素点数为128的图形
    plt.show()#显示图表
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
