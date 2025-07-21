# bank.py

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"{self.owner}'s account balance: ${self.balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0.0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0.0, overdraft_limit=100.0):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded.")
        self.balance -= amount


# Example usage:
if __name__ == "__main__":
    alice = SavingsAccount("Alice", 1000)
    bob = CheckingAccount("Bob", 200)

    alice.apply_interest()
    bob.withdraw(250)  # overdraft

    alice.deposit(300)
    bob.deposit(500)

    print(alice)
    print(bob)
