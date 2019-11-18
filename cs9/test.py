from vector import *
import os

def compare_file(path):
    # get txt file
    l = os.listdir(path)
    texts = [t for t in l if t.endswith(".txt")]
    #print table head
    print(" " * 15 + "|", end='')
    for text in texts:
        print("{:25}|".format(text),end="")
    print()
    d = {}
    for text in texts:
        print("{:15}|".format(text),end="")
        for t in texts:
            if not d.get(t):
                with open(t, 'r') as f:
                    content = f.read()
                d[t] = Sketch(content, 5, 100)
            s = d[text]
            t = d[t]
            print("{:>22}|".format(s.similarity(t)), end="")
        print("\n" + "-"*len(texts)*22)

