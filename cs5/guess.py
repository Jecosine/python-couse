import tkinter as tk
import tkinter.messagebox as ms
import socket


client = socket.socket()
status = False
def submit_answer():
    global client
    client.sendAll(answer.encode())
    print()
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

window = tk.Tk()
window.title("Guess")
window.geometry("300x200")

login = tk.Toplevel(window)
login.geometry("300x200")
login.title("Select Server")

server_ip = tk.StringVar()
nickname = tk.StringVar()
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


answer = tk.StringVar()
tk.Label(window, text="Answer").place(x = 10, y = 10)
text = tk.Entry(window, textvariable = answer)
text.place(x = 130, y = 10)

submit = tk.Button(window, text="Submit", command=submit_answer)
submit.place(x = 130, y = 50)
window.mainloop()
