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
    status = True
    login.destroy()
    return
def start_game():
    pass
def stop_game():
    pass
def giveup():
    pass
# main windows
window = tk.Tk()
window.title("Guess")
window.geometry("300x200")
# toolbar of main windows
menubar = tk.Menu(window)
# add selector game
gamemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Game', menu = gamemenu)
gamemenu.add_command(label='New', command = start_game)
gamemenu.add_command(label='Stop Game', command = stop_game)
gamemenu.add_command(label='Quit', command=window.quit)
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

tk.Label(window, text="Time").place(x = 10, y = 10)
text = tk.Entry(window, textvariable = answer)
answer = tk.StringVar()
tk.Label(window, text="Answer").place(x = 10, y = 10)
text = tk.Entry(window, textvariable = answer)
text.place(x = 130, y = 10)
# submit button
submit = tk.Button(window, text="Submit", command=submit_answer)
submit.place(x = 130, y = 50)
giveup = tk.Button(window, text="Give Up", command=giveup)
giveup.place(x = 130, y = 80)
window.mainloop()
