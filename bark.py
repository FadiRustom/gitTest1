class ATM:

    def __init__(self, balance ,bank_name):
        self.balance= balance
        self.bank_name = bank_name
        self.withdrawals_list=[]

    def withdraw(self,request):
        papers=[100,50,10,5,2]
        while request > 0:
            if request > self.balance :
                print(" can't give you all this money !!")
                break
            self.withdrawals_list.append(request)
            for i in papers:
                while request >= i:
                    print('give' +' '+ str(i))
                    # request+=1
                    self.balance-=i
                    request-=i
                    # if not request==0 :break
            request-=1

        print('Your Balance Is'+' '+ str(self.balance))
        return self.balance

    def show_withdrawals(self):
        for widthdrawals in self.withdrawals_list:
            print(widthdrawals)


balance1 = 1000
balance2 = 1000

atm1=ATM(balance1, 'Smart Bank')
atm2=ATM(balance2, 'Old Bank')

atm1.withdraw(300)
atm1.withdraw(500)
atm1.show_withdrawals()