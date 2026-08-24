from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, number, id) -> None:
        self.number = number
        self.id = id
        self.balance = 0

    def deposit(self, amount) -> int:
        if amount <= 0:
            return 1
        self.balance += amount
        return 0

    def bal(self) -> int:
        return self.balance

    def withdraw(self, amount) -> int:
        if amount <= 0:
            return 1
        self.balance -= amount
        return 0

class SavingsAccount(Account):
    minimum = 0
    def withdraw(self, amount) -> int:
        # check if withdrawal goes under minimum balance
        if self.balance - amount < self.minimum:
            return 2
        return super().withdraw(amount)

class CheckingAccount(Account):
    max_overdraft = 0
    def withdraw(self, amount) -> int:
        if amount - self.balance > self.max_overdraft:
            return 2
        return super().withdraw(amount)