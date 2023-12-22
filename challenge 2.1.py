class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        # Private attributes
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposit of ${amount} successful.")
        else:
            print("Invalid amount for deposit.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrawal of ${amount} successful.")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    # Method to display the account balance
    def display_balance(self):
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Balance: ${self.__account_balance:.2f}")


# Testing the BankAccount class
if __name__ == "__main__":
    # Create an instance of the BankAccount class
    account = BankAccount(account_number="123456789", account_holder_name="John Doe", initial_balance=1000)

    # Display initial balance
    account.display_balance()

    # Deposit money
    account.deposit(500)

    # Display balance after deposit
    account.display_balance()

    # Withdraw money
    account.withdraw(200)

    # Display balance after withdrawal
    account.display_balance()

    # Try to withdraw more than the current balance
    account.withdraw(2000)

    # Display balance after attempting to withdraw more than the current balance
    account.display_balance()
