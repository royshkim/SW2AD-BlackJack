class Dealer:
    def __init__(self):
        self.num = 0

    def addnumber(self, list):
        #리스트는 카드의 리스트
        self.num = 0
        #카드 숫자의 총합
        for i in range(0,len(list)):
            if list[i].isdigit():
                #숫자인지 검사
                if i%2 == 0:
                    self.num += int(list[i])
                    #뽑힌 카드의 숫자를 바로 더해준다.
                #else:
                    #pass
            elif list[i].isalpha() and list[i] != 'A':
                self.num += 10
            #else:
                #pass
        return self.num


    def hidecard(self, list):
        for i in range(2,len(list)):
            list[i] = '*'

