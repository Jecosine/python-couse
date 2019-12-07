import tkinter as tk
import tkinter.messagebox as ms
from GuessGame import GuessGame
import time
#instance of game is null
game = None
t = None

# functions
def start_game():
    global game
    global score
    global t
    global jumble
    
    game = GuessGame()
    game.start_game()
    jumble.set(game.jumble)
    score.set(game.score)
    t = time.time()

def stop_game():
    global game
    data = game.records
    panel = tk.Toplevel(window)
    panel.geometry("600x{0}".format(len(data)*100))    
    tk.Label(panel, text="Score: ").place(x = 10, y = 0)
    tk.Label(panel, text=str(game.score)).place(x = 50, y = 0)
    for i in range(len(data)):
        tk.Label(panel, text="Correct Answer:").place(x = 10, y = 30*i)
        tk.Label(panel, text=data[i]["word"]).place(x = 90, y = 30*i)
        tk.Label(panel, text="Your answer:").place(x = 200, y = 30*i)
        tk.Label(panel, text=data[i]["answer"]).place(x = 280, y = 30*i)
        tk.Label(panel, text="Result:").place(x = 350, y = 30*i)
        tk.Label(panel, text=data[i]["status"]).place(x = 400, y = 30*i)
    confirm = tk.Button(panel, text="OK", command=panel.quit)
    confirm.place(x = 130, y = 90 * len(data) + 50)

def submit_answer():
    global answer
    global t
    global score
    global winner
    global _current
    global jumble
    global status
    global answer
    _current.set(game.current)  
    if game.judge(answer.get()):
        ms.showinfo("Result","You are right!")
    else:
        ms.showinfo("Result","You are wrong!")
      
    time.sleep(2)
    game.new_turn()
    answer.set("")
    winner.set("Guessing...")
    jumble.set(game.jumble)
    
def giveup():
    global answer
    global winner
    global _current
    global jumble
    global status

    winner.set("You give up!")
    _current.set(game.current)
    game.new_turn()
    answer.set("")
    winner.set("Guessing...")
    jumble.set(game.jumble)
# GUI
window = tk.Tk()
window.title("Guess Game")
# set window size
window.geometry("400x300")
# make tool bar
menubar = tk.Menu(window)
gamemenu = tk.Menu(menubar, tearoff=0)
gamemenu.add_command(label="New Game", command=start_game)
gamemenu.add_command(label="Stop Game", command=stop_game)
gamemenu.add_command(label="Quit", command=window.quit)
menubar.add_cascade(label="Game", menu = gamemenu)
window.config(menu = menubar)

# main gui
#jumble
jumble = tk.StringVar()
tk.Label(window, text="Current Jumble:").place(x = 10, y = 30)
tk.Label(window, textvariable=jumble).place(x = 130, y = 30)
# #timer
# timer = tk.StringVar()
# timer.set('0')
# tk.Label(window, textvariable=timer).place(x = 130, y = 60)
#score
score = tk.StringVar()
score.set('0')
tk.Label(window, text="Score: ").place(x = 10, y = 0)
tk.Label(window, textvariable=score).place(x = 50, y = 0)
# correct 
_current = tk.StringVar()
_current.set("Answer Unpublish")
tk.Label(window, text="Last Answer:").place(x = 10, y = 90)
tk.Label(window, textvariable=_current).place(x = 130, y = 90)
#answer
answer = tk.StringVar()
tk.Label(window, text="Answer").place(x = 10, y = 120)
text = tk.Entry(window, textvariable = answer)
text.place(x = 130, y = 120)
# submit button
submit = tk.Button(window, text="Submit", command=submit_answer)
submit.place(x = 130, y = 150)
giveup = tk.Button(window, text="Give Up", command=giveup)
giveup.place(x = 130, y = 180)
#winner
winner = tk.StringVar()
winner_color = tk.StringVar()
winner.set('Guessing')
status = tk.Label(window, textvariable=winner)
status.place(x = 130, y = 0)


window.mainloop()