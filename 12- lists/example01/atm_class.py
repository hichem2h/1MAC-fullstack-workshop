class ATM :

    def __init__(self, balance, name):
        self.withdrawals_list = []
        self.name = name
        self.balance = balance

    def withdraw(self, request):
        self.print_sep('Current balance = {}'.format(self.balance), self.name)

        if   request > self.balance:
            print("Can't give you all this money !!")

        elif request < 0:
            print("More than zero plz!")

        else:
            self.withdrawals_list.append(request)
            self.balance -= request
            cash = [200, 100, 50, 20, 10, 5, 2, 1]
            for e in cash:
                while request >= e:
                    print 'give {}'.format(e)
                    request -= e

    def show_withdraws(self):
        self.print_sep('Withdraws Receipt', self.name)

        for withdrawal in self.withdrawals_list:
            print 'withdrawal: {}'.format(withdrawal)

    @staticmethod
    def print_sep(title, name):
        sep = '=' * 23

        print
        print sep
        print 'Welcome to {}'.format(name)
        print title
        print sep


if __name__ == '__main__':
    balance1 = 500
    balance2 = 1000

    atm1 = ATM(balance1, "Smart Bank")
    atm2 = ATM(balance2, "Baraka Bank")

    atm1.withdraw(277)
    atm1.withdraw(52)
    atm1.withdraw(1000)
    atm1.withdraw(-5)

    atm2.withdraw(654)
    atm2.withdraw(106)
    atm2.withdraw(900)

    atm1.show_withdraws()
    atm2.show_withdraws()
