def withdraw(available=500, requested=500):
    """Prints an ATM receipt.

    Keyword arguments:
    available - the available balance (default: 500)
    requested - the requested amount of cash to be withdrawn (default: 500)
    """
    available = int(available)
    requested = int(requested)

    print "CURRENT BALANCE: ", available
    print "AMOUNT TO BE WITHDRAWN: ", requested

    if (available < requested):
        print "Not enough balance"
    elif (requested <= 0):
        print "Please input a positive amount for the cash to be withdrawn"
    else:
        UNITS = [100, 50, 10, 5, 1]
        temp = requested
        i = 0
        print "UNIT\tAMOUNT"
        print "-" * len("UNIT"), "\t", "-" * len("AMOUNT")
        while (temp > 0):
            amount_of_unit = temp / UNITS[i]
            if (amount_of_unit > 0):
                print UNITS[i], "\t", amount_of_unit
                temp -= UNITS[i] * amount_of_unit
            i += 1
        print "BALANCE AFTER WITHDRAWAL: ", available - requested


# Tests
TESTS = [277, 201, -20, 150, 7, 501]
for idx, val in enumerate(TESTS):
    if (idx != 0):
        print
    withdraw(requested=val)
