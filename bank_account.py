class BankAccount():

    all_accounts = []
    
    def __init__(self, int_rate = 0.01, balance = 0,):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
        return self
    
    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            print(account)
        return cls


account1 = BankAccount()
account2 = BankAccount()

account1.deposit(100).deposit(200).deposit(300).withdrawal(50).yield_interest().display_account_info()
account2.deposit(200).deposit(800).withdrawal(300).withdrawal(23).withdrawal(142).withdrawal(93).yield_interest().display_account_info()

BankAccount.display_all_accounts()