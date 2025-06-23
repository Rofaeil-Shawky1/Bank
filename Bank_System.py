email = "rofa@gmail.com"
password = "12345"
balance = 0.0  

user_email = input("Enter your email: ")
user_pass = input("Enter your password: ")

if user_email == email and user_pass == password:
    print("Login successful!\n")
    
    while True:
        print("Please choose option:")
        print("1:Deposit")
        print("2:Withdraw")
        print("3:Check Balance")
        print("4:Exit")

        choice = input(">>> ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print("Deposit successful. New balance:", balance)

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            if amount > balance:
                print("Insufficient funds!")
            else:
                balance -= amount
                print("Withdrawal successful. Remaining balance: ",balance)

        elif choice == "3":
            print("Your current balance is: " , balance)

        elif choice == "4":
            print("Logged out. Thank you")
            break

        else:
            print("Invalid choice. Please try again")

else:
    print("Incorrect email or password")
