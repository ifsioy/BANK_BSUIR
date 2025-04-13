from typing import List
from src.domain.entities.bank import Bank
from src.domain.entities.user import User
from src.domain.enums import Role
from src.domain.exeptions import PermissionDeniedError
from src.infrastructure.repositories.bank_repository import SQLiteBankRepository
from src.infrastructure.repositories.user_bank_repository import SQLiteUserBankRepository


class BankService:
    def __init__(self):
        self.user_bank_repo = SQLiteUserBankRepository()
        self.bank_repo = SQLiteBankRepository()

    def get_all_banks(self) -> List[Bank]:
        return self.bank_repo.get_all()

    def get_user_banks(self, user_id: str) -> List[Bank]:
        return self.user_bank_repo.get_user_banks(user_id)

    def add_bank_to_user(self, user_id: str, bank_id: str):
        if not self.bank_repo.get_by_id(bank_id):
            raise ValueError("Банк с указанным ID не существует")

        user_banks = self.get_user_banks(user_id)
        if any(bank.id == bank_id for bank in user_banks):
            raise ValueError("Банк уже добавлен пользователю")

        self.user_bank_repo.add_user_bank(user_id, bank_id)

    def remove_bank_from_user(self, user_id: str, bank_id: str):
        user_banks = self.get_user_banks(user_id)
        if not any(bank.id == bank_id for bank in user_banks):
            raise ValueError("Банк не найден у пользователя")

        self.user_bank_repo.delete_user_bank(user_id, bank_id)

    def create_bank(self, user: User, name: str, bic: str) -> Bank:
        if Role.ADMIN not in user.roles:
            raise PermissionDeniedError("Требуются права администратора")

        new_bank = Bank(name=name, bic=bic)
        self.bank_repo.add(new_bank)
        return new_bank

    def delete_bank(self, user: User, bank_id: str):
        if Role.ADMIN not in user.roles:
            raise PermissionDeniedError("Требуются права администратора")

        self.bank_repo.delete(bank_id)