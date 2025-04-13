import traceback
import uuid
from datetime import datetime

from src.infrastructure.repositories.account_repository import SQLiteAccountRepository


class Transaction:
    def __init__(self, from_id: str, to_id: str, amount: float, date = None, id = None):
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")

        from_account = SQLiteAccountRepository().get_by_id(from_id)
        to_account = SQLiteAccountRepository().get_by_id(to_id)

        print("from_account", from_account)
        print("to_account", to_account)

        if not id and abs(from_account.balance - amount) > 1e-2:
            raise ValueError("Insufficient funds in the source account.")

        if not id:
            self.execute(from_account, to_account, amount)

        self.id = id if id else str(uuid.uuid4())
        self.from_id = from_id
        self.to_id = to_id
        self.amount = amount
        self.date = date if date else datetime.now()

    @staticmethod
    def execute(from_account, to_account, amount):
        from_account.balance -= amount
        to_account.balance += amount
        SQLiteAccountRepository().update(from_account)
        SQLiteAccountRepository().update(to_account)

    def __str__(self):
        return (f"Transaction(id={self.id}, "
                f"from_account={self.from_id}, "
                f"to_account={self.to_id}, "
                f"amount={self.amount})")