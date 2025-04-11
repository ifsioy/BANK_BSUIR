from src.domain.entities.account import Account

class Transaction:
    def __init__(self, from_account: Account, to_account: Account, amount: float):
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        if from_account.balance < amount:
            raise ValueError("Insufficient funds in the source account.")

        from_account.balance -= amount
        to_account.balance += amount

        self.transaction_id = 0
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount

    def __str__(self):
        return (f"Transaction(id={self.transaction_id}, "
                f"from_account={self.from_account.account_number}, "
                f"to_account={self.to_account.account_number}, "
                f"amount={self.amount})")