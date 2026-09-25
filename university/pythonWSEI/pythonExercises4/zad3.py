class BankAccount:
    def __init__(self, account_number, currency, bank, owner, balance=0):
        self.account_number = account_number
        self.currency = currency
        self.bank = bank
        self.__owner = owner
        self.__balance = balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, new_owner):
        self.__owner = new_owner

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    def __str__(self):
        return f"Account Number: {self.account_number}\nOwner: {self.__owner}\nBank: {self.bank}\nCurrency: {self.currency}\nBalance: {self.__balance}"

    def __len__(self):
        return self.__balance

    def __add__(self, other):
        if (
            isinstance(other, BankAccount)
            and self.bank == other.bank
            and self.currency == other.currency
            and self.__owner == other.owner
        ):
            new_balance = self.__balance + other.balance
            return BankAccount(self.account_number, self.currency, self.bank, self.__owner, new_balance)
        else:
            raise ValueError("Accounts cannot be added. They are not compatible.")

account1 = BankAccount("123456789", "USD", "PKO", "Alice", 1000)
account1.owner = "Alice2"
account1.balance = 1500
print(account1.owner)
print(account1.balance)
print("====")

account2 = BankAccount("987654321", "USD", "PKO", "Alice", 2000)
account2.owner = "Alice2"
account2.balance = 2500
print(account2.owner)
print(account2.balance)
print("========")

print(str(account1))
print("====")
print(len(account1))
print("========")
print(str(account2))
print("====")
print(len(account2))
print("========")

combined_account = account1 + account2
print(str(combined_account))