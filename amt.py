class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []
    def calcul(self,request):
        self.withdrawals_list.append(request)
        self.balance -= request
        notes =[100,50,10,5]
        for note in notes :
            while request >= note :
                request-=note
                print("give ", str(note))
        if request < 5:
            print("give " + str(request))
            request = 0
        return self.balance

    def withdraw(self, request):
        print("the name of bank is :",self.bank_name)
        print("the balance is",self.balance)
        if   request > self.balance:
            print("Can't give you all this money !!")
        elif request < 0:
            print("More than zero plz!")
        else:
            self.calcul(request)

    def show_withdrawals(self):
            for withdrawal in self.withdrawals_list:
                print(withdrawal)


balance1=500
balance2=1000
atm1=ATM(balance1,"smart_bank")
atm2=ATM(balance2,"baraka_bank")
atm1.withdraw(700)
atm1.withdraw(300)
print("the rest of balance for smart bank are",atm1.balance)
atm2.withdraw(500)
print("the rest of balance for baraka bank are",atm2.balance)
atm2.withdraw(257)
print("the rest of balance for baraka bank are",atm2.balance)
atm2.show_withdrawals()
