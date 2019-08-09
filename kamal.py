class ATM():
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.withdrawals_list = []

    def print_bank_name(self):
        print("Welcome to {} Bank".format(self.name))

    def show_withdrawals(self):
        print("=== This is All with withdrawals on {} Bank ===".format(self.name))
        for i in self.withdrawals_list:
            print(i)

    def withdraw(self, request):
        self.print_bank_name()
        requested = 0
        if request > self.balance:
            print("Can't give you all this money !!")

        elif request < 0:
            print("More than zero plz!")

        else:
            allowed_paper = [100, 50, 10, 5]
            requested = request
            self.withdrawals_list.append(request)
            print("[*] Request for {}$".format(request))
            for paper in allowed_paper:
                while requested >= paper:
                    requested -= paper
                    print("give {}".format(paper))
            if requested != 0:
                print("give {}".format(requested))
            print("[*] Request for {}$ Done".format(request))
            print("")
        return self.balance - requested


balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Barak")
atm2 = ATM(balance2, "AGB")

atm1.withdraw(188)
atm1.withdraw(200)
atm2.withdraw(566)
atm2.withdraw(275)

atm1.show_withdrawals()
atm2.show_withdrawals()