from src.domain.entities.transaction import Transaction
from src.domain.interfaces import ITransactionRepository, IAccountRepository
from src.domain.exeptions import PermissionDeniedError, TransactionNotFoundError
from src.domain.enums import Role
from src.infrastructure.repositories.account_repository import SQLiteAccountRepository
from src.infrastructure.repositories.transaction_repository import SQLiteTransactionRepository
from src.infrastructure.repositories.user_repository import SQLiteUserRepository


class TransactionService:
    def __init__(self):
        self.transaction_repo = SQLiteTransactionRepository()
        self.account_repo = SQLiteAccountRepository()
        self.user_repo = SQLiteUserRepository()

    def reverse_transaction(self, transaction_id: str):
        transaction = self.transaction_repo.get_by_id(transaction_id)
        if not transaction:
            raise TransactionNotFoundError()

        new_transaction = Transaction(
            from_id=transaction.to_id,
            to_id=transaction.from_id,
            amount=transaction.amount,
        )

        self.transaction_repo.add(new_transaction)

    def get_all(self):
        return self.transaction_repo.get_all()
