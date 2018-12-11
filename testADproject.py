import unittest

from card import Card
from dealer import Dealer
from joiner import Joiner

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Card()
        self.g2 = Dealer()
        self.g3 = Joiner()

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        for i in range(2):
            self.g1.mixcard()
        self.g2.hidecard(self.g1.cards)
        for j in range(2,len(self.g1.cards)):
            self.assertEqual(self.g1.cards[j], "*")
        self.assertEqual(len(self.g1.cards), 4)
        self.g1.cards.clear()
        self.g1.mixcard()
        self.assertEqual(len(self.g1.cards), 2)

    def add(self):
        self.g1.cards.clear()
        self.g1.cards = ['8','','K','']
        self.assertEqual(self.g2.addnumber(self.g1.cards), 18)
        self.g1.cards.clear()
        self.g1.cards = ['3', '','5','']
        self.assertEqual(self.g2.addnumber(self.g1.cards), 8)
        self.g1.cards.clear()
        self.g1.cards = ['7','','8','']
        self.assertEqual(self.g3.addnumber(self.g1.cards), 15)
        self.g1.cards.clear()
        self.g1.cards = ['6','','Q','']
        self.assertEqual(self.g3.addnumber(self.g1.cards), 16)





if __name__ == '__main__':
    unittest.main()