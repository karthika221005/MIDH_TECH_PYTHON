#3class bankAccount:  # creates a class named bankAccount
#      def __init__(self, owner, balance): #constructor method to initialize the owner and balance attributes
#           self.owner = owner 
#           self.__balance = balance
#        def show_balance(self):
#           print(f"Account owner: {self.owner}")
#           print(f"Account balance: {self.__balance}")
#account1 = bankAccount("Karthika", 1000)
#account1.show_balance()





class BankAccount:   # Creates a class named BankAccount

    def __init__(self, owner, balance):   # Constructor
        self.owner = owner
        self._account_type = "Savings"
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient funds or invalid amount")

    def show_balance(self):
        print(f"Account Balance: {self.__balance}")


# Creating an object
account1 = BankAccount("Karthika", 5000)

# Deposit money
account1.deposit(1000)

# Withdraw money
account1.withdraw(2000)

# Display balance
account1.show_balance()