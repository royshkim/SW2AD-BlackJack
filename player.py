class Player:
    def __init__(self):
        self.num = 0


    def addnumber(self, list):
        self.num = 0
        for i in range(0,len(list)):
            if list[i].isdigit():
                if i%2 == 0:
                    self.num += int(list[i])
                else:
                    pass
            elif list[i].isalpha() and list[i] != 'A':
                self.num += 10
            else:
                pass
        return self.num
