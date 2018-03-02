balance = 1000

def withdraw(balance, request):

    print("Your balance is: {0}$ and you requested {1}$.".format(balance,request))

    if request > balance or balance <= 0 or request <= 0:
        print("Invalid request or insufficient fund")
        return balance

    balance -= request

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

    if balance == 0:
        print("Out of money, please deposit to your balance")


    return balance
