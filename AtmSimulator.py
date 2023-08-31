class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hi How Can I Help You
        <> Press 1 To Create Pin
        <> Press 2 To Change Pin
        <> Press 3 To Check Balance
        <> Press 4 To Withdraw Money
        <> Press 5 To Deposit Money
        Press any other key to exit
        """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        elif user_input == '5':
            self.deposit()
        else:
            exit()

    def create_pin(self):
        user_pin = input("Enter pin : ")
        self.pin = user_pin
        user_balance = int(input("Enter Balance = "))
        self.balance = user_balance

        self.menu()

    def change_pin(self):
        old_pin = input("Enter your existing pin : ")
        if old_pin == self.pin:
            new_pin = input("Enter new pin = ")
            self.pin = new_pin
            print("Pin Changed Successfully")
        else:
            print("Credential Error")

        self.menu()

    def check_balance(self):
        user_pin = input("Enter your pin : ")
        if user_pin == self.pin:
            print("Your Balance Is ", self.balance)
        else:
            print("Invalid Pin")

        self.menu()

    def deposit(self):
        user_pin = input("Enter your pin : ")
        if user_pin == self.pin:
            amt = int(input("Enter Amount To Be Deposited = "))
            self.balance = self.balance+amt
            print("Deposit Successful")
            print("Updated Balance is : ",self.balance)

        else:
            print("Invalid Pin! Please Try Again")

        self.menu()

    def withdraw(self):
        user_pin = input("Enter your pin : ")
        if user_pin == self.pin:
            amt = int(input("Enter amount to be withdrawn = "))
            if amt <= self.balance:
                self.balance = self.balance - amt
                print("Withdrawn Successful")
                print("Remaining Balance is : ", self.balance)
            else:
                print("Doesn't have enough balance to withdraw")
        else:
            print("Invalid Pin! Please Try Again")

        self.menu()


obj = Atm()