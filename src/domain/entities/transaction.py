import uuid
from datetime import datetime

from src.infrastructure.repositories.account_repository import SQLiteAccountRepository


class Transaction:
    def __init__(self, from_id: str, to_id: str, amount: float, date = datetime.datetime.now(), id = str(uuid.uuid4())):
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")

        from_account = SQLiteAccountRepository.get_by_id(from_id)
        to_account = SQLiteAccountRepository.get_by_id(to_id)

        if from_account.balance < amount:
            raise ValueError("Insufficient funds in the source account.")

        from_account.balance -= amount
        to_account.balance += amount

        self.id = id
        self.from_id = from_id
        self.to_id = to_id
        self.amount = amount
        self.date = date

    def __str__(self):
        return (f"Transaction(id={self.id}, "
                f"from_account={self.from_id}, "
                f"to_account={self.to_id}, "
                f"amount={self.amount})")