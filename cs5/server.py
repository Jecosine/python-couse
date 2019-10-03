import socketserver
import random
import time
class GuessGame:
    def __init__(self, wordlist="words.txt"):
        self.__init__()
        self.current = ""
        self.current_index = -1
        self.bingo = False
        self.wordlist = []
        self.wordlist_path = wordlist

        random.seed(time.time())
    def init_wordlist(self):
        with open(self.wordlist, "r") as f:
            content = f.read()
            content = [word.strip() for word in content.split("\n") if len(word.strip())>1]
        self.wordlist = content
    def instance_word(self):
        random
    

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        try:
            while True:
                self.data=self.request.recv(1024)
                print("{} send:".format(self.client_address),self.data)
                if not self.data:
                    print("connection lost")
                    break
                if len(self.data) and self.data[:2] == b"A:":
                    res = self.data[3:]
                    self.judge(res)
                else:

               # self.request.sendall(self.data.upper())
        except Exception as e:
            print(self.client_address,"Disconnect")
        finally:
            self.request.close()
    def setup(self):
        print("before handle, connection established：", self.client_address)

    def finish(self):
        print("finish run  after handle")

if __name__=="__main__":
    HOST,PORT = "0.0.0.0",9999
    server=socketserver.TCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()
