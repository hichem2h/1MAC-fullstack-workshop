available = 500
requested = 187

print("CURRENT BALANCE: " + str(available))
print("AMOUNT TO BE WITHDRAWN: " + str(requested))

if (available < requested):
    print("Not enough balance")
elif (requested <= 0):
    print("Please input a positive amount for the cash to be withdrawn")
else:
    UNITS = [100, 50, 10, 5, 1]
    temp = requested
    i = 0

    print("UNIT\tAMOUNT")
    print("-" * len("UNIT") + "\t" + "-" * len("AMOUNT"))

    while (temp > 0):
        amount_of_unit = temp / UNITS[i]
        if (amount_of_unit > 0):
            print(str(UNITS[i]) + "\t" + str(amount_of_unit))
            temp -= UNITS[i] * amount_of_unit
            i += 1
print("BALANCE AFTER WITHDRAWAL: " +  str(available - requested))
