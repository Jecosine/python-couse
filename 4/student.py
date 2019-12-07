import random

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def generate():
    name = "路人{}"
    mylist = []
    for i in range(10):
        score = random.randint(70, 101)
        age = random.randint(17,19)
        mylist.append(Student(name.format(i), age, score))
    return mylist
def show_list(l):
    print("index\tname\tage\tscore")
    for i in range(len(l)):
        print("{}\t{}\t{}\t{}".format(i, l[i].name, l[i].age, l[i].score))
    
def sort_list(l):
    l = sorted(l, key = lambda s : s.score, reverse = True)
    return l

        
if __name__ == "__main__":
    l = generate()
    print("Before sort:")
    show_list(l)
    print("After sort:")
    l = sort_list(l)
    show_list(l)
