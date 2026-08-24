from account import *
from typing import Dict, List
class User(ABC):
    id: int
    name: str
    email: str
    username: str
    password: str
    user_type: str
    def login(self, username, password) -> int:
        if self.username == username and self.password == password:
            return 0
        return 1

    def print_self(self) -> None:
        print(f"Name: {self.name}, ID: {self.id}, Email: {self.email}, Type: {self.user_type}")

class Customer(User):
    user_type = "cust"
    def __init__(self, id, name, email, branch_id, username, password, accounts: Dict[int,Account] = {}) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.branch_id = branch_id
        self.username = username
        self.password = password
        self.accounts: Dict[int, Account] = accounts

    def add_account(self, account: Account) -> int:
        if account.id in self.accounts:
            return 1
        self.accounts[account.id] = account
        return 0

    def print_account(self, id) -> None:
        account = self.accounts[id]
        print(f"Id: {account.id}, Number: {account.number}, Type: {account.account_type}, Balance: {account.balance}")

    def print_accounts(self) -> None:
        for id in self.accounts.keys():
            self.print_account(id)

    def get_account(self, id) -> Account | None:
        if id in self.accounts:
            return self.accounts[id]
        return None

    def deposit(self, account_id, amount) -> int:
        account = self.get_account(account_id)
        # if id is not in accounts
        if account is None:
            return 3
        return account.deposit(amount)

    def withdraw(self, account_id, amount) -> int:
        account = self.get_account(account_id)
        # if id is not in accounts
        if account is None:
            return 3
        return account.withdraw(amount)

    def transfer(self, source_id, dest_id, amount) -> int:
        if amount <= 0:
            return 1
        source = self.get_account(source_id)
        dest = self.get_account(dest_id)
        # if id is not in accounts
        if source is None or dest is None:
            return 3
        code = source.withdraw(amount)
        # check whether withdrawal succeeded
        if code:
            return code
        code = dest.deposit(amount)
        if code:
            return 3 + code
        return 0



class Admin(User):
    user_type = "admin"
    def __init__(self, id, name, email, username, password) -> None:
        self.id = id
        self.name = name
        self.email = email        
        self.username = username
        self.password = password
