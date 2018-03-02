class ATM:

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):
        sep = "=" * 35
        print("Welcome to " + self.bank_name)
        print("Current balance = %d" % self.balance)

        print(sep)

        if request > self.balance:
            print("Can't give you all this money !!")

        elif request < 0:
            print("More than zero plz!")

        else:
            self.balance -= request
            ATM.process_request(request)

        print(sep + "\n")


    @staticmethod
    def process_request(request, alowed_papers=[100, 50, 10, 5, 2, 1]):
        for paper in alowed_papers:
            while request >= paper:
                print('give ' + str(paper))
                request -= paper


if __name__ == '__main__':

    balance1 = 500
    balance2 = 1000

    atm1 = ATM(balance1, "Smart Bank")
    atm2 = ATM(balance2, "Baraka Bank")

    atm1.withdraw(277)
    atm1.withdraw(800)

    atm2.withdraw(100)
    atm2.withdraw(2000)
