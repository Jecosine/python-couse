import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def gen(d):
    t = []
    cols = d.columns
    for i in range(len(cols)-1):
        temp = list(cols[:-1])
        temp.pop(i)
        [t.append([cols[i], j]) for j in temp]
    print(t)
    return t



iris = pd.read_csv("iris.csv",error_bad_lines=False)
# generate two cols
t = gen(iris)
colors = ['r', 'y','b']
species = iris.Species.unique()
_, ax = plt.subplots(3,4, figsize=(10,10))

for j in range(12):
    plt.subplot(3, 4, j+1)
    for i in range(len(species)):
        plt.scatter(iris.loc[iris.Species == species[i], t[j][0]], iris.loc[iris.Species == species[i],t[j][1]], s = 35, c = colors[i], label = species[i])
        
    plt.title("{} vs {}".format(t[j][0], t[j][1]))
    plt.xlabel(t[j][0])
    plt.ylabel(t[j][1])
    plt.grid(True, linestyle=":", alpha=0.5)
    plt.legend(loc="lower right")
    
plt.show()
