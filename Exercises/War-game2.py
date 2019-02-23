from random import shuffle

class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [None, None, "2", "3", "4", "5",
              "6", "7", "8", "9" ,"10",
              "Jack", "Queen", "King", "Ace"]

    def __init__(self, s, v):
        self.suit = s
        self.value = v

    def __gt__(self, other):
        if self.value > other.value:
            return True
        elif self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False

    def __lt__(self, other):
        if self.value < other.value:
            return True
        elif self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        string = self.values[self.value] + " of " + self.suits[self.suit]
        return string



class Deck:
    def __init__(self):
        self.cards = []
        for s in range(0, 4):
            for v in range(2, 15):
                self.cards.append(Card(s, v))

    def shuffle(self):
        shuffle(self.cards)
 

class Player:
    def __init__(self, n):
        self.number = n
        self.n = input("Type in player %d name: " % n)
        self.score = 0
        self.card = None

    def __repr__(name):
        return self.n

    def draw_card(self, deck):
        self.card = deck.pop()


class Game:
    def __init__(self):
        self.p1 = Player(1)
        self.p2 = Player(2)

    def play(self):
        print("beginning War game!")
        self.deck = Deck()
        self.p1.score = 0
        self.p2.score = 0
        cards = self.deck.cards
        shuffle(cards)
        a = ""
        while len(cards) > 1:
            a = input("q to quit. Any key to play:")
            if a == "q":
                print("Game over")
                break
            self.p1.draw_card(cards)
            self.p2.draw_card(cards)
            print(self.p1.n,"drew",self.p1.card,self.p2.n,"drew",self.p2.card)
            if self.p1.card > self.p2.card:
                self.p1.score += 1
                print(self.p1.n,"wins this round")
            elif self.p1.card < self.p2.card:
                self.p2.score += 1
                print(self.p2.n,"wins this round")
            print("scores:",
                  self.p1.n,self.p1.score,"-",self.p2.score,self.p2.n)
        if self.p1.score > self.p2.score:
            print(self.p1.n,"wins the game!")
        elif self.p1.score < self.p2.score:
            print(self.p2.n,"wins the game!")
        else:
            print("No one is winner")


game = Game()

while True:
    game.play()
