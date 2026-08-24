from user import *
class Branch:
    users: Dict[int, User]
    def __init__(self, id, name, users = {}) -> None:
        self.id = id
        self.name = name
        self.users = users

    def print_users(self) -> None:
        for user in self.users.values():
            user.print_self()