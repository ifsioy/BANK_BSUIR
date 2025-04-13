from src.application.services.transaction_validator import TransactionValidator
from src.domain.entities.account import Account
from src.domain.entities.transaction import Transaction
from src.domain.enums import Status
from src.domain.interfaces import (
    IAccountRepository,
    ITransactionRepository,
    ITransactionValidator
)
from src.infrastructure.repositories.account_repository import SQLiteAccountRepository
from src.infrastructure.repositories.transaction_repository import SQLiteTransactionRepository


class AccountOperationService:
    def __init__(self):
        self.account_repo = SQLiteAccountRepository()
        self.transaction_repo = SQLiteTransactionRepository()
        self.validator = TransactionValidator()

    def deposit(self, account_id: str, amount: float):
        account = self._get_valid_account(account_id)
        self.validator.validate_deposit(amount)

        account.balance += amount
        self.account_repo.update(account)

        transaction = Transaction(
            amount=amount,
            from_id="0",
            to_id=account_id,
        )
        self.transaction_repo.add(transaction)

    def withdraw(self, account_id: str, amount: float):
        account = self._get_valid_account(account_id)
        self.validator.validate_withdrawal(account, amount)

        account.balance -= amount
        self.account_repo.update(account)

        transaction = Transaction(
            amount=amount,
            from_id=account_id,
            to_id="0"
        )
        self.transaction_repo.add(transaction)

    def transfer(self, from_account_id: str, to_account_id: str, amount: float):
        from_account = self._get_valid_account(from_account_id)
        to_account = self._get_valid_account(to_account_id)

        self.validator.validate_transfer(from_account, to_account, amount)

        self.account_repo.update(from_account)
        self.account_repo.update(to_account)

        transaction = Transaction(
            amount=amount,
            from_id=from_account_id,
            to_id=to_account_id
        )
        self.transaction_repo.add(transaction)

    def get_updated_account(self, account_id) -> Account:
        return self.account_repo.get_by_id(account_id)

    def get_transaction_history(self, account_id: str) -> list[Transaction]:
        return self.transaction_repo.get_by_account_id(account_id)

    def _get_valid_account(self, account_id: str) -> Account:
        account = self.account_repo.get_by_id(account_id)
        if not account:
            raise Exception("NO ACCOUNT")
        if account.status != Status.ACTIVE.value:
            raise Exception("ACCOUNT IS NOT ACTIVE")
        return account