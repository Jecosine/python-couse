import random
import copy
import tkinter as tk
import tkinter.messagebox as ms
class Game:
    def __init__(self):
        self.board = [[]]
        self.current = 1
        self.d = {1: 'computer', 4: 'player'}
    def init_board(self):
        self.board = [[0 for j in range(3)] for i in range(3)]
    def judge(self, board, current):
        for i in range(3):
            if sum(board[i]) == 3*current or sum([board[j][i] for j in range(3)]) == 3*current:
                print(sum(board[i]))
                return True
        if sum([board[i][i] for i in range(3)])==current*3 or sum([board[2-i][i] for i in range(3)]) == 3*current:
            return True
        return False
    def tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return False
        return True        
    def place(self, p, sboard, *args):
        if sboard[p[0]][p[1]] != 0:
            return False
        if len(args) != 0:
            sboard[p[0]][p[1]] = args[0]
        else:
            sboard[p[0]][p[1]] = self.current
        return True

    def render(self,b):
        for i in range(3):
            for j in range(3):
                print("%d "%b[i][j], end="")
            print()
    def bot(self):
        print("bot")
        m = [[i, j] for i in range(3) for j in range(3) if self.board[i][j] == 0]
        for i in m:
            
            sboard = copy.deepcopy(self.board)
            self.place(i, sboard, 4)
            if self.judge(sboard, 4):
                print(i)                
                # print(i[0],i[1])
                self.board[i[0]][i[1]] = 1
                return
            sboard = copy.deepcopy(self.board)
            self.place(i, sboard, 1)
            if self.judge(sboard, 1): 
                
                self.board[i[0]][i[1]] = 1
                return
        m = random.choice(m)
        self.place(m, self.board)
        return 
    def start(self):
        self.init_board()
        while(True):
            self.render(self.board)
            if self.current == 1:
                print("Robot's turn:")
                self.bot() 
                
            else:
                x, y = [int(i) for i in input("It's your turn: ").split(" ")]
                while(x not in range(3) or y not in  range(3) or self.board[x][y] != 0):
                    print("Occupied, choose another place please")
                    x, y = [int(i) for i in input("It's your turn: ").split(" ")]
                self.place((x, y), self.board)
              
            if self.judge(self.board, self.current):
                print("{} win".format(self.d[self.current]))
                self.render(self.board)
                break
            self.current = 4 if self.current == 1 else 1
            if(self.tie()):
                print("Tie!")
                break

class Gui():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("200x150")
        self.p = tk.Frame(self.window)
        self.p.pack(side=tk.TOP)
        self.game = Game()
        self.game.init_board()          
        self.group= [[0,0,0] for i in range(3)]
        self.vs = [[tk.StringVar() for i in range(3)] for j in range(3)]
        self.init_grid(self.game.board)      
        self.render()
    def place(self, p):
        print(p)
        if self.game.judge(self.game.board, 1):
            ms.showinfo("Status","computer win")
        if(self.game.tie()):
            ms.showinfo("Status","TIE!")
            self.game.init_board()
            self.bot()
            self.game.current = 4
            self.render()
        self.render()  
        if self.game.current == 4:
            if not self.game.place(p, self.game.board):
                return                                
            if self.game.judge(self.game.board, self.game.current):
                
                print("{} win".format(self.game.d[self.game.current]))
                self.game.init_board()
                self.bot()
                self.render()
                self.game.current = 4
            self.game.current = 1
        
            if(self.game.tie()):
                ms.showinfo("Status","TIE!")
                self.game.init_board()
                self.game.current = 4
                self.bot()
                self.render()
            else:
                self.bot()
                self.game.current = 4
    def bot(self):
        self.game.bot()
        self.render()  
    def get_func(self, p):
        i, j = p
        funcs = [self.f_1,self.f_2,self.f_3,self.f_4,self.f_5,self.f_6,self.f_7,self.f_8,self.f_9]
        return funcs[i*3 + j]
    def f_1(self):
        self.place((0,0))
    def f_2(self):
        self.place((0,1))
    def f_3(self):
        self.place((0,2))
    def f_4(self):
        self.place((1,0))
    def f_5(self):
        self.place((1,1))
    def f_6(self):
        self.place((1,2))
    def f_7(self):
        self.place((2,0))
    def f_8(self):
        self.place((2,1))
    def f_9(self):
        self.place((2,2))



    def init_grid(self, board):
        for i in range(3):
            for j in range(3):
                b = tk.Button(self.p, textvariable=self.vs[i][j], command=self.get_func((i, j)), width=5, height=2, relief=tk.FLAT)
                b.grid(row=i, column=j)
                self.group[i][j] = b
    def render(self):
        for i in range(3):
            for j in range(3):

                self.vs[i][j].set('X' if self.game.board[i][j] == 4 else 'O' if self.game.board[i][j] == 1 else '')

        
if __name__ == "__main__":
    g =Gui()
    g.bot()
    g.game.current = 4
    g.window.mainloop()


