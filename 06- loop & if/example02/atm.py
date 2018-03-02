money = 500
request = 227
cash = [100, 50, 20, 10, 5, 2, 1]

if money < request:
    print('Request refused (not enough money): ' + str(money) + ' available')

elif request < 0 :
    print('Request should be more than zero')

else :
    remainder = money - request
    for e in cash:
        while request >= e:
            print('Give: ' + str(e))
            request -= e
    print('Request Finished: '  + str(remainder) + ' available')
