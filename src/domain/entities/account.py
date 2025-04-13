import uuid

class Account:
    def __init__(self, user_id: str, balance: float, bank_id: str, id = None, status: str = "pending"):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")

        self.id = id if id else str(uuid.uuid4())
        self.user_id = user_id
        self.balance = balance
        self.bank_id = bank_id
        self.status = status

    def __str__(self):
        return (f"Account(id={self.id}, "
                f"user={self.user_id}, "
                f"balance={self.balance}, "
                f"bank={self.bank_id})")