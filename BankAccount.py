class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")

        self.__balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0 or amount > self.__balance:
            raise ValueError(
                "Withdrawal amount must be positive "
                "and less than or equal to the current balance."
            )

        self.__balance -= amount
        print(f"Withdrawn {amount}. New balance: {self.__balance}")


my_account = BankAccount("David", 55000)

my_account.deposit(5000)
my_account.withdraw(2000)

print(
    f"Owner is {my_account.owner} "
    f"and balance is {my_account.balance}"
)