class ATM:

    def __init__(self, balance, bank_name):
        self.withdrawal_list = []
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):
        print("Welcome to {0}".format(self.bank_name))
        print("Your balance is: {0}$ and you requested {1}$.".format(
            self.balance, request))

        if self.balance <= 0:
            print("Can't withdraw, out of balance, please deposit")

        elif request > self.balance or request <= 0:
            print("Invalid request or insufficient fund")

        else:
            self.balance -= request
            self.withdrawal_list.append(request)
            self.process_request(request)

    def show_withdrawals(self):
        index = 1
        for withdrawal in self.withdrawal_list:
            print("{0} withdrawal No.{1}: {2}$".format(self.bank_name, index, withdrawal))
            index += 1

    @staticmethod
    def process_request(request):
        while request > 0:
            if request >= 100:
                print("give 100")
                request -= 100
            elif request >= 50:
                print("give 50")
                request -= 50
            elif request >= 10:
                print("give 10")
                request -= 10
            elif request >= 5:
                print("give 5")
                request -= 5
            else:
                print("give {0}".format(request))
                request -= request
