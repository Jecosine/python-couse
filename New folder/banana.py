import matplotlib.pyplot as plt
import numpy as np
import csv
import time, random

# read csv file
def loadcsv(path):
    data = []
    with open(path, 'r') as f:
        content = csv.reader(f)
        for i in content:
            data.append(float(i[0]))
    return data

def loadcsv_2(path):
    data = []
    with open(path, 'r') as f:
        content = csv.reader(f)
        for i in content:
            data.append((int(i[0]), int(i[1])))
    return data
# process data into a dict
def pr_data():
    scores = loadcsv("data.csv")
    scores_data = {}
    for i in scores:
        scores_data[int(i)] = scores_data.get(int(i), 0) + 1
    return scores_data
def pr_data_5():
    scores = loadcsv("data.csv")
    scores_data = {}
    for i in scores:
        scores_data[int(i)//5] = scores_data.get(int(i)//5, 0) + 1
    return scores_data
def data_test(style):
    # setting x data
    data = np.array([i for i in range(10)])
    # setting y data
    y_data = np.power(data, 3)
    # use dark style
   
    #plt.style.use(style)
    fig, ax = plt.subplots(figsize=(5,5))
    ax.set_title(style)
    ax.bar(data, y_data)
    # show the y data on bar
    for a,b in zip(data, y_data):
        plt.text(a, b-57, "%d"%b, ha='center', va='bottom', fontsize=10, color=(1,1,1))
    plt.show()

#generate random data
def gen(n):
    data = []
    for i in range(n):
        data.append(random.randint(0, 100))
    return data
def fix(t):
    return t
def gen2(d):
    data = []
    for i in d:
        t = i[1] + random.randint(-30, 30)
        # judge whether reach border
        t = 1 if t < 1 else 200 if t > 200 else t
        data.append((i[0], i[1], t))
    return data
# show data
def show2():
    data = gen(100)
    fig, ax = plt.subplots()
    ax.set_xticks(range(0, 100, 5))
    ax.bar(range(0, 100), data, 0.5, alpha=0.5, color='b')
    plt.show()
def show3():
    data = loadcsv_2("data2.csv")
    fig, ax = plt.subplots()
    x = np.array([i+1 for i in range(len(data))])
    ax.set_xticks(range(1,11))
    # x-0.2 and x+0.2 make two bar stand on sides of value
    ax.bar(x-0.2, [i[0] for i in data], 0.4, alpha=0.5, color='r')
    ax.bar(x+0.2, [i[1] for i in data], 0.4, alpha=0.5, color='b')
    for a in x:
        a = a-1
        ax.text(a - 0.2 + 1, data[a][0], "%d"%data[a][0], ha='center', va='bottom', fontsize=10)
        ax.text(a + 0.2 + 1, data[a][1], "%d"%data[a][1], ha='center', va='bottom', fontsize=10)
    ax.legend(["This Term","Last Term"], loc='upper left')
    # set grid
    ax.grid(True, linestyle=':', alpha=0.6)
    plt.show()
def show4():
    data = gen2(loadcsv_2("data2.csv"))
    fig, ax = plt.subplots()
    x = np.array([i+1 for i in range(len(data))])
    ax.set_xticks(range(1,11))
    # x-0.2 and x+0.2 make two bar stand on sides of value
    ax.bar(x-0.2, [i[0] for i in data], 0.2, alpha=0.5, color='r')
    ax.bar(x, [i[1] for i in data], 0.2, alpha=0.5, color='g')
    ax.bar(x+0.2, [i[2] for i in data], 0.2, alpha=0.5, color='b')
    for a in x:
        a = a-1
        ax.text(a - 0.2 + 1, data[a][0] + 0.2, "%d"%data[a][0], ha='center', va='bottom', fontsize=10)
        ax.text(a + 1, data[a][1] + 0.2, "%d"%data[a][1], ha='center', va='bottom', fontsize=10)
        ax.text(a + 0.2 + 1, data[a][2] + 0.2, "%d"%data[a][2], ha='center', va='bottom', fontsize=10)
    ax.legend(["This Term","Last Term", "The Term before last Term"], loc='upper left')
    # set grid
    ax.grid(True, linestyle=':', alpha=0.6)
    plt.show()
# show data
def show_data():
    data = pr_data_5()
    fig = plt.figure()
    ax = plt.axes()
    # x axis
    x = [i*5 for i in data.keys()]
    ax.set_xticks([i for i in range(50, 101, 5)])
    # hide origin x axis
    ax.xaxis.set_major_formatter(plt.NullFormatter()) 
    ax.bar(x, data.values(), 3, alpha=0.5, color='b')
    # show the y data on bar
    for a,b in zip(x, data.values()):
        plt.text(a, b + 0.2, "%d"%b, ha='center', va='bottom', fontsize=10)
        # show x axis by text
        plt.text(a, -5, "%d~%d"%(a, a+5), ha='center', va='bottom', fontsize=10)
    plt.show()


def all_style():
    styles = plt.style.available
    for i in range(9):
        data_test(styles[i])
    plt.show()

data_test("nnn")
