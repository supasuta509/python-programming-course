# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice =="1":
            print(f"Your balance is {balance} THB")
        elif choice =="2":
            amount = float(input("Enter amountto withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrawal successfull. New balance: {balance} THB")
            else:
                print("Insufficient balance")
        elif choice == "3":
            amount = float(input("Enter amount to deposit:"))
            balance += amount
            print(f"Deposit successfil. New balance; {balance} THB")
        elif choice == "4":
            print("Thank you for using our ATM simulation.")
            break               
else:
    print("Invalid PIN")