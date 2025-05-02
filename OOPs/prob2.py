class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ ₹{amount} deposited. New balance: ₹{self.balance}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("❌ Insufficient balance.")
        else:
            self.balance -= amount
            print(f"✅ ₹{amount} withdrawn. Remaining balance: ₹{self.balance}")

    def transfer(self, amount, target_account):
        if amount <= 0:
            print("❌ Transfer amount must be positive.")
        elif amount > self.balance:
            print("❌ Transfer failed. Insufficient balance.")
        else:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"✅ ₹{amount} transferred to {target_account.holder_name}.")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Balance: ₹{self.balance}")

# Example usage
if __name__ == "__main__":
    acc1 = BankAccount("101", "Alice", 5000)
    acc2 = BankAccount("102", "Bob", 3000)

    acc1.deposit(2000)
    acc1.withdraw(1500)
    acc1.transfer(1000, acc2)

    print("\n📘 Final Account States:")
    acc1.display()
    acc2.display()