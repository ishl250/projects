class BankAccount:
    def __init__(self, owner, balance=100):
        self.owner = owner
        self.balance = balance
        print(f"Account created for {self.owner} with balance: {self.balance} Rwf")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return
        self.balance += amount
        print(f"Deposited {amount} Rwf. New balance: {self.balance} Rwf")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return
        if self.balance - amount < 100:
            print(f"Cannot withdraw {amount} Rwf. Minimum balance of 100 Rwf must be maintained.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} Rwf. New balance: {self.balance} Rwf")

# Example usage:
account = BankAccount("Ish Licky")

# Deposit money
account.deposit(int(input("Deposit amount: ")))

# Withdraw money
account.withdraw(int(input("Withdraw amount: ")))

# Attempt to withdraw too much
account.withdraw(int(input("Withdraw amount: ")))
