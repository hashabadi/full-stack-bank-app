class Account:
    def __init__(self, number, id) -> None:
        self.number = number
        self.id = id
        self.balance = 0

    def deposit(self, amount) -> int:
        if amount <= 0:
            return 1
        self.balance += amount
        return 0

    def withdraw(self, amount) -> int:
        self.balance -= amount
        return 0
