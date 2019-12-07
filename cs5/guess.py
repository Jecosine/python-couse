import tkinter as tk
import tkinter.messagebox as ms
import socket
import json


client = socket.socket()
status = False
point = 0
def submit_answer():
    global client
    client.sendall(("A:" + answer.get()).encode())
    res = client.recv(1024)
    if res == "True":
        point += 1
    answer.set("")
    print(res)
def parse(s):
    s = [i.strip() for i in s.strip().split(":")]
    if len(s) != 2:
        return False
    else:
        return s[0], int(s[1])

def connect_server():
    global client
    global status
    global score
    global _current
    global jumble
    global winner
    s = server_ip.get()
    _ = parse(s)
    if not _:
        status = False
        ms.showerror('Error', 'Invalid server address')
        return
    try:
        client.connect(_)
    except Exception as e:
        status = False
        ms.showerror('Error connecting server', '{0}'.format(e))
        return
    else:
        status = True
        login.destroy()
        while True:
            data = client.recv(1024)
            try:
                data = json.loads(data)
                keys = data.keys()
            except:
                pass
            else:
                # Status code: 
                # 1 : new turn
                # 2 : post result
                # 3 : game over
                # data:
                # score int
                # jumble string
                # current string
                status = int(data['status'])
                jumble.set(data['jumble'])
                score.set(data['score'])
                _current.set(data['current'])
                winner.set(data['winner'])


    
    return
def start_game():
    global nickname
    global client
    data = {
        'status' : 1,
        'nickname': nickname.get() 
    }
    client.sendall(json.dumps(data).encode())

def stop_game():
    pass
def giveup():
    pass
# main windows
window = tk.Tk()
window.title("Guess")
window.geometry("300x300")
# toolbar of main windows
menubar = tk.Menu(window)
# add selector game
gamemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Game', menu = gamemenu)
gamemenu.add_command(label='New', command = start_game)
gamemenu.add_command(label='Stop Game', command = stop_game)
gamemenu.add_command(label='Quit', command=window.quit)
window.config(menu = menubar)
# login windows
login = tk.Toplevel(window)
login.geometry("300x200")
login.title("Select Server")

server_ip = tk.StringVar()
nickname = tk.StringVar()
server_ip.set("10.129.15.37:9999")
tk.Label(login, text="Server IP: ").place(x = 10, y = 10)
tk.Label(login, text="Nickname: ").place(x = 10, y = 50)
# ip bar
ip_bar = tk.Entry(login, textvariable = server_ip)
ip_bar.place(x = 130, y = 10)
# nickname bar
nickname_bar = tk.Entry(login, textvariable = nickname)
nickname_bar.place(x = 130, y = 50)

confirm = tk.Button(login, text = "Connect", command = connect_server)
confirm.place(x = 130, y = 90)


#jumble
jumble = tk.StringVar()
tk.Label(window, text="Current Jumble:").place(x = 10, y = 30)
tk.Label(window, text=jumble.get()).place(x = 130, y = 30)
#timer
timer = tk.StringVar()
timer.set('0')
tk.Label(window, text=timer.get()).place(x = 130, y = 60)
#score
score = tk.StringVar()
score.set('0')
tk.Label(window, text="Score: ").place(x = 10, y = 0)
tk.Label(window, text=score.get()).place(x = 50, y = 0)
#winner
winner = tk.StringVar()
winner.set('Guessing')
tk.Label(window, text=winner.get()).place(x = 130, y = 0)
# correct 
_current = tk.StringVar()
_current.set("Unpublished")
tk.Label(window, text="Correct Answer:").place(x = 10, y = 90)
tk.Label(window, text=_current.get()).place(x = 130, y = 90)
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
window.mainloop()
