import tkinter as tk
import socket


client = socket.socket()
def submit_answer():
    var = text.get()
    print(var)
def parse(s):
    s = server_ip.get()
def connect_server():
    global client
    client.connet()

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


text = tk.Entry(window, show = None)
text.place(x = 130, y = 10)



submit = tk.Button(window, text="Submit", width = 5, height = 1, command=submit_answer)
submit.pack()
window.mainloop()
