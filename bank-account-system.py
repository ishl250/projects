import os
from fpdf import FPDF
from datetime import datetime

# -----------------------------
# Bank Classes
# -----------------------------
class BankAccount:
    """Base class representing a bank account."""
    def __init__(self, owner, balance=1000):
        self.__owner = owner
        self.__balance = balance
        self.__transactions = []  # Encapsulation: private transaction log

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def get_transactions(self):
        return self.__transactions

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        self.__transactions.append({
            "type": "Deposit",
            "amount": amount,
            "fee": 0,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        print(f"{self.__owner} deposited {amount} Rwf. New balance: {self.__balance} Rwf")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.__balance - amount < 100:
            print(f"Cannot withdraw {amount} Rwf. Minimum balance of 100 Rwf must be maintained.")
        else:
            self.__balance -= amount
            self.__transactions.append({
                "type": "Withdraw",
                "amount": amount,
                "fee": 0,
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            print(f"{self.__owner} withdrew {amount} Rwf. New balance: {self.__balance} Rwf")


class SavingsAccount(BankAccount):
    """Savings account with a withdrawal fee (polymorphism example)."""
    def withdraw(self, amount):
        fee = 10  # Fee for withdrawal
        total_amount = amount + fee
        print(f"Note: A withdrawal fee of {fee} Rwf applies.")
        if self.get_balance() - total_amount < 100:
            print(f"Cannot withdraw {amount} Rwf + {fee} Rwf fee. Minimum balance of 100 Rwf must be maintained.")
            return
        # Perform withdrawal including fee
        super().withdraw(total_amount)
        # Update last transaction to include fee properly
        self.get_transactions()[-1]['fee'] = fee
        self.get_transactions()[-1]['amount'] = amount  # actual withdrawn amount without fee


# -----------------------------
# PDF Report Generator
# -----------------------------
def generate_pdf(account):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    folder = os.path.join(desktop, "BankReports")
    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = os.path.join(folder, f"{account.get_owner()}_report.pdf")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Bank Report for {account.get_owner()}", ln=True, align="C")
    pdf.set_font("Arial", "", 12)
    pdf.ln(10)

    # Summary
    balance = account.get_balance()
    deposits = sum(txn['amount'] for txn in account.get_transactions() if txn['type'] == 'Deposit')
    withdrawals = sum(txn['amount'] for txn in account.get_transactions() if txn['type'] == 'Withdraw')
    fees = sum(txn['fee'] for txn in account.get_transactions())
    pdf.cell(0, 10, f"Current Balance: {balance} Rwf", ln=True)
    pdf.cell(0, 10, f"Total Deposited: {deposits} Rwf", ln=True)
    pdf.cell(0, 10, f"Total Withdrawn: {withdrawals} Rwf", ln=True)
    pdf.cell(0, 10, f"Total Fees Paid: {fees} Rwf", ln=True)
    pdf.ln(10)

    # Transaction History
    pdf.cell(0, 10, "Transaction History:", ln=True)
    pdf.ln(5)
    for txn in account.get_transactions():
        pdf.multi_cell(0, 8, f"{txn['type']}: {txn['amount']} Rwf, Fee: {txn['fee']} Rwf, On: {txn['timestamp']}")

    pdf.output(filename)
    print(f"PDF report generated: {filename}")


# -----------------------------
# Main Program
# -----------------------------
accounts = {}

while True:
    print("\n=== Real Banking System ===")
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")
    choice = input("Enter choice (1-3): ")

    if choice == '1':
        name = input("Enter account owner name: ")
        if name in accounts:
            print("Account already exists.")
        else:
            accounts[name] = SavingsAccount(name)
            print(f"Account created for {name}.")

    elif choice == '2':
        name = input("Enter account owner name: ")
        if name not in accounts:
            print("Account does not exist.")
            continue
        account = accounts[name]

        while True:
            print(f"\n--- Account Menu for {account.get_owner()} ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Balance")
            print("4. Show Transactions")
            print("5. Generate PDF Report")
            print("6. Back to Main Menu")
            print("7. Exit Program")
            sub_choice = input("Enter choice (1-7): ")


            if sub_choice == '1':
                try:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                except ValueError:
                    print("Please enter a valid number.")
            elif sub_choice == '2':
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Please enter a valid number.")
            elif sub_choice == '3':  # Show Balance
                print(f"\n--- Balance Summary for {account.get_owner()} ---")
                balance = account.get_balance()
                deposits = sum(txn['amount'] for txn in account.get_transactions() if txn['type'] == 'Deposit')
                withdrawals = sum(txn['amount'] for txn in account.get_transactions() if txn['type'] == 'Withdraw')
                fees = sum(txn['fee'] for txn in account.get_transactions())
                print(f"Current Balance: {balance} Rwf")
                print(f"Total Deposited: {deposits} Rwf")
                print(f"Total Withdrawn: {withdrawals} Rwf")
                print(f"Total Fees Paid: {fees} Rwf")
            elif sub_choice == '4':  # Show Transactions
                print(f"\n--- Transaction History for {account.get_owner()} ---")
                txns = account.get_transactions()
                if not txns:
                    print("No transactions yet.")
                else:
                    for i, txn in enumerate(txns, start=1):
                        print(f"{i}. {txn['type']}: {txn['amount']} Rwf, Fee: {txn['fee']} Rwf, On: {txn['timestamp']}")
            elif sub_choice == '5':
                generate_pdf(account)
            elif sub_choice == '6':
                break
            elif sub_choice == '7':
                print("Exiting program.")
                exit()  # immediately exit the program
            else:
                print("Invalid choice. Please select 1-6.")

    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please select 1-3.")
