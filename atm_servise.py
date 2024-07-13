balance = 1000000
print(f"Your balance is {balance} $")

while True:
    print("1. Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("0. Exit")
    choice = input("Enter your choice : ")

    if choice == '1':
        print(f"Your balance is : {balance} $")
        break
    elif choice == '2':
        value = float(input("Enter withdraw value : "))
        if value > 0 and value <= balance:
            commission = value * 0.01  # 1% commission
            balance -= value + commission
            print(f"Your money was successfully withdrawn. Commission: {commission:.2f} $")
        else:
            print("Sorry, that value is not available!")
    elif choice == '3':
        value = float(input("Enter deposit value : "))
        if value > 0 and value < 10000000:
            commission = value * 0.01
            balance += value - commission
            print(f"Money successfully deposited. Commission: {commission:.2f} $")
        else:
            print("Please, enter valid value !")
    elif choice == '0':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again")
