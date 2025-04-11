from src.domain.entities.user import User
from src.domain.entities.bank import Bank

class Account:
    def __init__(self, account_number: str, user: User, balance: float, bank: Bank):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")

        self.account_number = account_number
        self.user = user
        self.balance = balance
        self.bank = bank

    def __str__(self):
        return (f"Account(account_number={self.account_number}, "
                f"user={self.user.full_name}, "
                f"balance={self.balance}, "
                f"bank={self.bank.name})")