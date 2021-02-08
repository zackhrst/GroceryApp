class BankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def deposit_money(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transfer(self, amount, destination):
        self.withdraw(amount)
        destination.deposit_money(amount)



checking_account = BankAccount(100, "123BAC")
checking_account.deposit_money(50)
print(checking_account.balance)
checking_account.withdraw(20)
print(checking_account.balance)

savings_account = BankAccount("321ABC", 500)
checking_account.transfer(50, savings_account)

# Checking account  Savings Account
# 100                 500

# Transfer 200 from Savings to Checking   
#     -withdraw 200 form Savings
#     -deposit 200 into checking