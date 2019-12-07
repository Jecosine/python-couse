class Chess:
    def __init__(self,n):
        self.n = n
        self.checker = [[0 for i in range(n)]for j in range(n)]
        self.answer = []
        self.count = 0
    def solution(self):
        # 求解过程
        if self.istrue():
            self.backtrace(self.checker,0)
            return self.answer
        else:
            print("无解")

    def istrue(self):
        #棋盘有解的条件
        if self.n >= 4:
            return True
        else:
            return False

    def backtrace(self,checker,row):
        #回溯
        if row == self.n:
            print(self.answer)
            self.answer.pop(-1)
            self.count += 1
            return True
        isplaced = False
        for col in range(0,self.n):
            if (self.isvalid(checker,row,col)):
                checker[row][col] = 1
                isplaced = True
                self.answer.append(col)
                self.checker.append(self.tolist(checker))
                _ = self.backtrace(checker,row + 1)
                if not _:
                    self.answer.pop(-1)
                checker[row][col] = 0
            # col += 1
        if not isplaced:            
            return False
    def tolist(self,checker):
        list = []
        for i in range(0,len(checker)):
            list.append(checker[i])
            # i += 1
        return list

    def isvalid(self,checker,x,y):
        #判断下棋的位置是否合法
        for i in range(0,x+1):
            for j in range(0, self.n):
                # print (i, j)
                if checker[i][j] == 1 and (j == y or abs(x-i) == abs(y-j)):
                    return False
        return True

ch = Chess(3)
ch.solution()
print(ch.count)



