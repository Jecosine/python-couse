import matplotlib.pyplot as plt
import numpy as np
import csv
import time, random
# read csv file
# 读取csv文件~~
def loadcsv(path):
    data = []
    with open(path, 'r') as f:
        content = csv.reader(f)
        for i in content:
            data.append(float(i[0]))
    return data
# 处理数据，计算每个分数段多少人
def pr_data_5():
    # 先从csv里面读取数据
    scores = loadcsv("data.csv")
    # 新建一个字典准备储存统计数据
    scores_data = {}
    for i in scores:
        # //的意思是整除，比如两个数是分别是64，61，属于60~65，这个时候//5之后，两个数都是12了，都在12这个区间段~，
        # 所以我们就可以把0到100通过//5分成20段
        # 然后这个就可以计算在20段里面每个段的人数了
        scores_data[int(i)//5] = scores_data.get(int(i)//5, 0) + 1
    # 最后的这个scores_data里面就是这样滴：
    # {18: 6, 19: 1, 15: 71, 16: 55, 17: 25, 14: 89, 13: 51, 12: 8}
    # 第19（18+1）段有6人，第20段有1人，第16段55人。。。。。。
    return scores_data

# show data
def show_data():
    # 获取统计好的数据
    data = pr_data_5()
    # 创建子图
    fig, ax = plt.subplots()
    # x axis
    # 因为是统计的时候是0到20，除过5的，要乘个5变回来
    x = [i*5 for i in data.keys()]
    #设置坐标轴是每五个单位一个点，从50 到 100
    ax.set_xticks([i for i in range(50, 101, 5)])
    # hide origin x axis
    # 把x坐标轴藏起来
    ax.xaxis.set_major_formatter(plt.NullFormatter()) 
    # 绘制直方图
    ax.bar(x, data.values(), 3, alpha=0.5, color='b')
    # 显示直方图上每个柱的数据
    for a,b in zip(x, data.values()):
        plt.text(a, b + 0.2, "%d"%b, ha='center', va='bottom', fontsize=10)
        # show x axis by text
        # 让x轴显示成x~x的样子，比如60~65
        plt.text(a, -5, "%d~%d"%(a, a+5), ha='center', va='bottom', fontsize=10)
    #显示图
    plt.show()

show_data()