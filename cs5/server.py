import socketserver
import random
import time
import json
class GuessGame:
    def __init__(self, wordlist="words.txt", player=[]):
        self.__init__()
        self.room = 0
        self.current = ""
        self.current_index = -1
        self.bingo = False
        self.wordlist = []
        self.wordlist_path = wordlist
        self.player = []
        self.turn_winner = None
        random.seed(time.time())

    def add_player(self,player):
        self.player.append({
            'ip': player[0],
            'nickname': player[1],
            'score': 0
        })
    def init_wordlist(self):
        with open(self.wordlist, "r") as f:
            content = f.read()
            content = [word.strip() for word in content.split("\n") if len(word.strip())>1]
        self.wordlist = content
    
    def instance_word(self):
        self.current_index = random.range(len(self.wordlist)-1)
        self.current = self.wordlist[self.current_index]
        self.jumble_word = self.jumble(self.current)
        
    def judge(self, post):
        if (type(post) == type(b'')):
            post = post.decode()
        if post == self.current:
            self.bingo == True

    def jumble(self, word):
        jb = ''
        while len(word) > 1:
            i = random.randrange(len(word))
            jb += word[i]
            word = word[:i] + (word[i+1:] if (i + 1 < len(word)) else '')
        jb += word
        return jb
        

class MyTCPHandler(socketserver.BaseRequestHandler):
    # while got connected
    # status code
    # 1 -> start game
    # 2 -> close game, return rank
    # 3 -> post data
    def __init__(self):
        self.__init__()
        self.clients = []
    def add_client(self, client):
        self.clients.append({
            'ip': client[0],
            'nickname': client[1]
        })
    def handle(self):
        global game
        try:
            while True:
                self.data = self.request.recv(1024)
                # print connected host
                print("{} send:".format(self.client_address),self.data)
                if not self.data:
                    print("connection lost")
                    break
                else:
                    self.data = json.loads(self.data.decode())
                    status = self.data['status']
                    if int(status) == 1:
                       client.sendall()

                if len(self.data) and self.data[:2] == b"A:":
                    res = self.data[3:]
                    self.judge(res)


               # self.request.sendall(self.data.upper())
        except Exception as e:
            print(self.client_address,"Disconnect")
        finally:
            self.request.close()
    def setup(self):
        print("before handle, connection established：", self.client_address)

    def finish(self):
        print("finish run  after handle")
game = GuessGame()
if __name__=="__main__":
    HOST,PORT = "0.0.0.0",9999
    game = GuessGame()
    server=socketserver.TCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()
