from branch import *
def main():
    # seed data
    alice_accounts: Dict[int, Account] = {1: CheckingAccount(1, 1),
                                          2: SavingsAccount(2, 2)}
    alice = Customer(1, "Alice", "a@mail.com", 1, "alice", "Alice123", alice_accounts)
    alice_accounts[2].deposit(100)

    bob_accounts: Dict[int, Account] = {3: CheckingAccount(3, 3),
                                        4: CheckingAccount(4, 4),
                                        5: SavingsAccount(5, 5)}
    bob = Customer(2, "Bob", "b@mail.com", 2, "bob", "Bob123", bob_accounts)
    bob_accounts[3].deposit(300)

    branch = Branch(1, "Citi", {1: alice, 2: bob})
    auth = 1
    real_user = None
    while auth:
        username = input("Please input your username: ")
        for user in branch.users.values():
            if user.username == username:
                real_user = user
                break
        password = input("Please input your password: ")
        if real_user is None or real_user.password != password:
            print("incorrect username or password")
        else:
            print(f"Successfully authenticated as {real_user.username}")
            auth = 0

    if isinstance(real_user, Customer):
        while True:
            option = int(input("""Pick an option:
            1. View accounts
            2. View a specific account
            3. Deposit
            4. Withdraw
            5. Transfer
            """))
            match option:
                case 1:
                    real_user.print_accounts()
                case 2:
                    real_user.print_account(int(input("Please input account id: ")))
                case 3:
                    real_user.deposit(int(input("Please input account id: ")), int(input("Please input deposit amount: ")))
                case 4:
                    real_user.withdraw(int(input("Please input account id: ")), int(input("Please input withdrawal amount: ")))
                case 5:
                    source = int(input("Please input source account id: "))
                    dest = int(input("Please input destination account id: "))
                    amount = int(input("Please input transfer amount: "))
                    real_user.transfer(source, dest, amount)

    elif isinstance(real_user, Admin):
        pass

main()