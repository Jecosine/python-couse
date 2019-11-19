from vector import *
import os
import random
def generate():
    # add a-z and A-Z
    l = [chr(i) for i in range(65, 65 + 26)]
    l += [chr(i) for i in range(97, 97 + 26)]
    # add space and comma and dot, increase space count to improve proprability
    l += [' ', ' ', ' ', ' ', ',', '.']
    s = ''
    for i in range(400):
        s += random.choice(l)
    return s

def compare_file(path):
    # get txt file
    l = os.listdir(path)
    texts = [t for t in l if t.endswith(".txt")]
    #print table head
    print(" " * 15 + "|", end='')
    for text in texts:
        print(text.center(15) + '|',end="")
    print("\n" + "-"*(len(texts) + 1)*16)
    d = {}
    for text in texts:
        print(text.center(15),end="|")
        for t in texts:
            if not d.get(t):
                with open(path + '/' + t, 'r') as f:
                    content = f.read()
                d[t] = Sketch(content, 5, 2000)
            s = d[text]
            t = d[t]
            print("{:.6f}".format(s.similarity(t)).center(15), end="|")
        print("\n" + "-"*(len(texts) + 1)*16)

if __name__ == "__main__":
    compare_file("data")