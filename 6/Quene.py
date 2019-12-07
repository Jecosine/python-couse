class Quene:
    # initialize
    def __init__(self):
        self.q = []
        self.len = 0
    # e is the element to get in
    def one_in_quene(self, e):
        self.q.append(e)
        self.len += 1
    # e is a list contain elements
    def more_in_quene(self, e):
        self.q += e[:]
        self.len += len(e)
    
    def out_quene(self):
        if len(self.q) > 0:
            self.len -= 1
            return self.q.pop(0)        
        else:
            print("Quene is Empty")
            return None
    def head_quene(self):
        return self.q[0]

    def tail_quene(self):
        return self.q[-1]

    def show_quene(self):
        print(str(self.q))
    
    def isempty(self):
        if len(self.q) > 0:
            return False
        return True
    def length(self):
        return self.len

if __name__ == "__main__":
    q = Quene()
    q.more_in_quene([1,2,3,4,5])
    q.show_quene()
    # get length
    print("Length: {}".format(q.length()))
    # head of quene
    q.head_quene()
    # tail of quene
    q.tail_quene()
    print("Is Empty?: {}".format(q.isempty()))
    # pop elements
    print("\nAfter popping")
    for i in range(6):
        e = q.out_quene()
        if e:
            print("Out quene element: {}".format(e))
    # print length
    print("Length: {}".format(q.length()))
    print("Is Empty?: {}".format(q.isempty()))