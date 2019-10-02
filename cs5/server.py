import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                self.data=self.request.recv(1024)
                print("{} send:".format(self.client_address),self.data)
                if not self.data:
                    print("connection lost")
                    break
                if len(self.data) and self.data[:2] == "A:":
                    res = self.data[3:]
                    print(res)
                
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