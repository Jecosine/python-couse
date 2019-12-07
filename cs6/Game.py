import time, random

class Game:
    # init game data
    def __init__(self):
        self.state = False
        self.cards = []
        self.house_hand = []
        self.house_count = 0
        self.player_count = 0
        self.player_hand = []
        self.values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '1':10, 'J':10, 'Q':10, 'K':10, 'A':11}
    # start game init game info
    def start_game(self):
        # clear cards on hand
        self.__init__()
        self.get_cards()
        # deliver 2 cards to house and player
        for i in range(4):
            self.deliver_cards((i + 1) % 2)
        self.print_status()
        r = self.get_reply("Get cards(Y or y for yes, other for no)? ")
        while r in ['y','Y']:
            # deliver to player
            self.deliver_cards(1)
            # print status
            self.print_status()
            # calculate points of player
            r = self.count(1)
            if r > 21:
                print("Game Over! House win(Player more than 21)")       
                self.state = True
                return
            r = self.get_reply("Get cards(Y or y for yes, other for no)? ")
        else:
            print("Player Standing, house get cards")
            self.robot()
            r = self.count(0)
            if r > 21:
                print("Player Win!(House more than 21)")       
                self.state = True
                return
        # Judgement of winner
        if self.player_count > self.house_count:
            print("Player Win!!!")
        else:
            print("House Win!!!")

    def print_status(self):
        # print player cards
        print()
        print("Player cards:", end = '')
        for i in self.player_hand:
            print(" {}".format(i), end = "")
        print()
        # print house cards
        print("House cards: ", end = '')
        for i in self.house_hand:
            print(" {}".format(i), end = "")
        print()

    def robot(self):
        while self.house_count <= 17:
            self.deliver_cards(0)
            self.count(0)
            self.print_status()    

    #get reply
    def get_reply(self, s):
        return input(s)

    # generate cards
    def get_cards(self):
        suits = ['♠','♣','♥','♦']
        ranks = [str(i) for i in range(2, 11)] + ['J','K','A']
        for i in suits:
            for j in ranks:
                self.cards.append("{}{}".format(j, i))
        random.shuffle(self.cards)
        
    # deliver cards
    def deliver_cards(self, t):
        card = self.cards.pop()
        if t:
            self.player_hand.append(card)
        else:
            self.house_hand.append(card)
        return card

    # count point
    # 0 -> house
    # 1 -> player
    def count(self, t):
        cards = self.player_hand if t else self.house_hand
        total = 0
        count = 0
        for i in cards:
            if i[0] != 'A':
                total += self.values[i[0]]
            else:
                count += 1
        while count:
            total += 1 if (total + 11 > 21) else 11
            count -= 1
        if t:
            self.player_count = total
        else:
            self.house_count = total
        return total
    
if __name__ == "__main__":
    game = Game()
    r = input("Start Game ?")
    while r in ['y','Y']:
        game.start_game()
        r = input("Start Game ?")
            


        