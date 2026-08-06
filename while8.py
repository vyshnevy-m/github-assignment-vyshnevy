#atm machine code#
while True:
    c = int(input("1.Balance 2.Deposit 3.Withdraw 4.Exit: "))

    if c == 4:
        break
    elif c == 1:
        print("Balance")
    elif c == 2:
        print("Deposit")
    elif c == 3:
        print("Withdraw")