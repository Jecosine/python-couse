import numpy as np
stack = []

count = 0
state = []
N = 5
def solve():
    global count
    global state
    global stack
    global N
     
    i = 0
 
    l = 0
    stack = [-1]
    B = state[-1].copy()
    #state.append(B)
    while stack : 
        if l == N:            
            count += 1
            print(stack[1:])
            stack.pop(-1)
            l -= 1
            B = state.pop(-1)
        i = 0        
        flag = False    
        # print(stack)    
        while i < N:                     
            if B[l, i] == 0:
                flag = True
                stack.append(i)  
                        
                # mark
                B[:, i] = 1
                for j in range(0, N - l):
                    if (i - j >= 0):
                        B[l + j, i - j] = 1
                    if (i + j < N):
                        B[l + j, i + j] = 1
                l += 1
                state.append(B.copy())
                # print("Append")
                # print(B)
                # print()
                break
            else:        
                i += 1
        if not flag:
            # print("Exit")
            # print(B)
            x = stack.pop(-1) 
            state.pop(-1)
            l -= 1
            if not state:
                break
            state[-1][l, x] = 2
            B = state[-1].copy()
            # print("current")
            # print(B)
            
N = 5         
canvas = np.zeros((N,N), dtype = np.int8)
state = [canvas]
B = state[-1]


solve()
# print(B)
print(count)




