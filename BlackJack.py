from card import Card
from dealer import Dealer
from player import Player
import sys
import random
from PyQt5.QtWidgets import *

class BlackJack(QWidget):

    def __init__(self):
        super().__init__()
        self.score = 5000
        self.initUI()

    def initUI(self):
        self.lbl0 = QLabel('Score: ', self)
        self.line0 = QLineEdit('', self)
        self.line0.setReadOnly(True)
        self.line0.setText(str(self.score))
        self.lbl1 = QLabel('Bet: ', self)
        self.line1 = QLineEdit('', self)
        StartButton = QPushButton('Newgame', self)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.lbl0)
        hbox.addWidget(self.line0)
        hbox.addWidget(self.lbl1)
        hbox.addWidget(self.line1)
        hbox.addWidget(StartButton)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        self.bet = QLabel('Dividend rate', self)
        self.line2 = QLineEdit('',self)
        self.line2.setReadOnly(True)
        HitButton = QPushButton('Hit', self)
        StandButton = QPushButton('Stand', self)
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.bet)
        hbox2.addWidget(self.line2)
        hbox2.addWidget(HitButton)
        hbox2.addWidget(StandButton)
        vbox.addLayout(hbox2)

        self.lbl2 = QLabel('Dealer\'s card', self)
        self.dealerText = QTextEdit('',self)
        self.dealerText.setReadOnly(True)
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.lbl2)
        hbox3.addWidget(self.dealerText)
        vbox.addLayout(hbox3)

        self.lbl3 = QLabel('Player\'s card', self)
        self.playerText = QTextEdit('', self)
        self.playerText.setReadOnly(True)
        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        hbox4.addWidget(self.lbl3)
        hbox4.addWidget(self.playerText)
        vbox.addLayout(hbox4)

        self.lbl4 = QLabel('Result      ', self)
        self.resultText = QTextEdit('', self)
        self.resultText.setReadOnly(True)
        hbox5 = QHBoxLayout()
        hbox5.addStretch(1)
        hbox5.addWidget(self.lbl4)
        hbox5.addWidget(self.resultText)
        vbox.addLayout(hbox5)

        StartButton.clicked.connect(self.startgame)
        HitButton.clicked.connect(self.hitclicked)
        StandButton.clicked.connect(self.standclicked)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 360, 300)
        self.setWindowTitle('BlackJack')
        self.show()

    def startgame(self):
        self.resultText.clear()
        self.card = Card()
        self.dealer = Dealer()
        self.player = Player()
        self.rate = []#배당률

        for i in range (10,26):
            self.rate.append(i/10)

        self.line2.setText(str(random.choice(self.rate)))

        try:
            self.playerText.clear()
            #자산에서 입력한 점수를 뺴고 표시해준다.
            self.score -= int(self.line1.text())
            self.line0.setText(str(self.score))

            #딜러가 두장을 뽑는다.
            for i in range(2):
                self.card.mixcard()
            #딜러의 카드 숫자를 합친 변수 numb
            self.numb = self.dealer.addnumber(self.card.cards)
            #ACE카드가 뽑혔을때의 딜러 카드
            for l in range(0, len(self.card.cards)):
                if self.card.cards[l] == 'A':
                    if self.numb <= 10:
                        self.numb += 11
                    else:
                        self.numb += 1
            print(self.numb)
            #딜러의 카드 숫자합이 16보다 작거나 같을때 계속 뽑는다.
            while self.numb <= 16:
                print(self.numb)
                self.card.mixcard()
                self.numb = self.dealer.addnumber(self.card.cards)
                for m in range(0,len(self.card.cards)):
                    if self.card.cards[m] == 'A':
                        if self.numb <= 10:
                            self.numb += 11
                        else:
                            self.numb += 1
            #딜러창을 띄울때 사용하는 변수
            self.number = str(self.numb)
            print(self.card.cards)
            self.dealercard=self.card.returncard()



            #self.s=self.card.returncard()


            #숨기는 매서드 사용
            self.dealer.hidecard(self.card.cards)
            #hide card를 거친 딜러의 카드를 표시
            self.dealerText.setText(self.card.returncard())
            #플레이어 카드를 뽑기위해 딜러의 카드를 삭제
            self.card.cards.clear()

            #플레이어가 카드를 두장 뽑아놓기만 하면 됨
            for j in range(2):
                self.card.mixcard()
                self.playerText.setText(self.card.returncard())

        except:
            self.resultText.setText("Your input score is empty.")


    def hitclicked(self):
        self.card.mixcard()
        self.playerText.setText(self.card.returncard())


    def standclicked(self):
        # 넘버2 플레이어의 카드 합을 계산하는 변수
        self.numb2 = self.player.addnumber(self.card.cards)
        # 딜러의 스타트 클릭 메서드를 실행하고. 스탠드를 눌러서 경기를 끝냈을때 띄움

        self.dealerText.setText(str(self.dealercard)+"\n"+str(self.number))


        for m in range(0, len(self.card.cards)):
            if self.card.cards[m] == 'A':
                if self.numb2 <= 10:
                    self.numb2 += 11
                else:
                    self.numb2 += 1
        self.playerText.setText(str(self.card.returncard())+"\n"+str(self.numb2))
        self.endgame()



    def endgame(self):
        print(self.card.cards)
        self.dealerscore = 21 - self.numb
        self.playerscore = 21 - self.numb2
        print(self.playerscore)

        if self.dealerscore >= 0:
            if self.playerscore >= 0:
                if self.dealerscore > self.playerscore:
                    self.resultText.setText('you win!')
                    self.line0.setText(str(int(self.score + int(self.line1.text()) * float(self.line2.text()))))
                elif self.dealerscore < self.playerscore:
                    self.resultText.setText('dealer win!')
                else:
                    self.resultText.setText('draw')
                    self.line0.setText(str(int(self.score + int(self.line1.text()))))
            else:
                self.resultText.setText('bust!')
        else:
            if self.playerscore >= 0:
                self.resultText.setText('you win!')
                self.line0.setText(str(int(self.score + int(self.line1.text()) * float(self.line2.text()))))
            else:
                self.resultText.setText('bust!')

        if len(self.dealercard) == 4:
            if self.dealerscore == 0:
                self.dealerText.setText("blackjack!")
                if len(self.card.cards) == 4:
                    if self.playerscore == 0:
                        self.playerText.setText("blackjack!")
                        self.resultText.setText("draw")
                        self.line0.setText(str(int(self.score + int(self.line1.text()))))
                    else:
                        self.resultText.setText("dealer win!")
                else:
                    self.resultText.setText("dealer win!")

        if len(self.card.cards) == 4:
            if self.playerscore == 0:
                self.playerText.setText("blackjack!")
                if len(self.dealercard) != 4 or self.dealerscore != 0:
                    self.resultText.setText("you win!")
                    self.line0.setText(str(int(self.score + int(self.line1.text()) * float(self.line2.text()))))
                else:
                    self.resultText.setText("draw")



        '''
        self.dealerscore = 21-self.numb
        self.playerscore = 21-self.numb2

        #self.playerscore = 21-self.player.addnumber(self.card.cards)

        #딜러가 10과 11로 두장의 카드로 블랙잭일때
        if len(self.card.cards) == 4:
            if self.dealerscore == 0:
                self.dealerText.setText("Blackjack!")
                if len(self.card.cards) == 4:
                    if self.playerscore == 0:
                        self.playerText.setText("blackjack!")
                        self.resultText.setText("draw")
                    else:
                        self.resultText.setText("dealer win!")
                else:
                    self.resultText.setText("dealer win!")

        if self.dealerscore >= 0:
            if self.playerscore >= 0:
                if self.dealerscore > self.playerscore:
                    self.resultText.setText('you win!')
                    #베팅액에 배당을 곱해서 자산에 더해준다.
                    self.line0.setText(str(int(self.score + int(self.line1.text()) * float(self.line2.text()))))
                elif self.dealerscore < self.playerscore:
                    self.resultText.setText('dealer win!')
                else:
                    self.resultText.setText('draw')
                    #비겼을때는 원금을 돌려준다
                    self.line0.setText(str(int(self.score + int(self.line1.text()))))
            #플레이어가 21이 넘어갔을때
            else:
                self.resultText.setText('bust!')
        else:
            #딜러의 점수가 21을 초과했을때
            #플레이어는 21보다 작기만하면 플레이어 승리
            if self.playerscore >= 0:
                self.resultText.setText('you win!')
                self.line0.setText(str(int(self.score + int(self.line1.text()) * float(self.line2.text()))))
            #플레이어, 딜러 둘다 21이 넘었을때
            else:
                self.resultText.setText('bust!')
                
        '''
        #이 구문을 안쓰면 이겨도 차감만되고 베팅액만 깎임
        self.score = int(self.line0.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BlackJack()
sys.exit(app.exec_())
