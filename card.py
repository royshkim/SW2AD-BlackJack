import random

class Card:
    def __init__(self):
        self.numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.shapes = ["♤","♢","♡","♧"]
        self.cards = []
        self.card = ''

    def mixcard(self):
        #random 함수를 이용하여 카드의 숫자와 모양을 선택.
        self.cards.append(random.choice(self.numbers))
        self.cards.append(random.choice(self.shapes))

    def returncard(self):
        self.card = ''.join(self.cards)
        return self.card
