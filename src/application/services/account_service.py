from src.domain.entities.account import Account
from src.domain.enums import Role, Status
from src.domain.exeptions import PermissionDeniedError, AccountFrozenError
from src.infrastructure.repositories.account_repository import SQLiteAccountRepository
from src.infrastructure.repositories.user_repository import SQLiteUserRepository
from src.logger import logger


class AccountService:
    def __init__(self):
        self.account_repo = SQLiteAccountRepository()

    def get_user_accounts(self, user_id: str, bank_id: str) -> list[Account]:
        return self.account_repo.get_user_accounts(user_id, bank_id)

    def create_account(self, user_id: str, bank_id: str, initial_balance: float) -> Account:
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")

        new_account = Account(
            user_id=user_id,
            bank_id=bank_id,
            balance=initial_balance
        )
        logger.info("New account created", new_account)
        return self.account_repo.add(new_account)

    def delete_account(self, account_id: str):
        self.account_repo.delete(account_id)

    def set_status(self, user_id: str, account_id: str, status: Status):
        if not self._is_manager_or_admin(user_id):
            raise PermissionDeniedError("Требуются права менеджера или администратора")

        account = self.account_repo.get_by_id(account_id)
        if not account:
            raise ValueError("Счет не найден")

        self.account_repo.change_status(account_id, status)

    def _is_manager_or_admin(self, user_id: str) -> bool:
        user = SQLiteUserRepository().get_by_id(user_id)
        return any(role in user.roles for role in [Role.MANAGER, Role.ADMIN])

    def get_inactive_accounts(self, bank_id: str) -> list[Account]:
        return self.account_repo.get_all_inactive(bank_id)

