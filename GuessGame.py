import random, time

class GuessGame:
    def __init__(self):
        self.words = []
        self.current = ""
        self.current_index = -1
        self.jumble = ""
        self.records = []
        self.score = 0
    def load_words(self, path):
        with open(path,'r') as f:
            content = f.read()
        self.words = [i.strip() for i in content.split("\n") if len(i.strip())>0]
    def start_game(self):
        self.load_words("words.txt")
        random.seed(time.time())
        self.new_turn()
    def new_turn(self):
        
        self.current = random.choice(self.words)
        self.jumble_word()
    def jumble_word(self):
        s = self.current
        jumble = ""
        while len(s) > 1:
            i = random.randrange(0, len(s))
            jumble += s[i]
            # while choose last one
            s =  s[:i] + (s[i+1:] if i != len(s) - 1 else "")
        jumble += s
        print(self.current, jumble)
        self.jumble = jumble
    def judge(self, answer):
        data = {}
        data["word"] = self.current
        data["answer"] = answer
        if answer == self.current:            
            data["status"] = "Accept"
            self.records.append(data)
            self.score += 100

            return True
        else:
            data["status"] = "Wrong"
            self.records.append(data)
            return False
