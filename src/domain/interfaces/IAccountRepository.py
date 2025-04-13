from src.domain.entities.account import Account


class IAccountRepository:
    def add(self, account: Account):
        raise NotImplementedError

    def get_by_id(self, account_id: str):
        raise NotImplementedError

    def update(self, account: Account):
        raise NotImplementedError

    def delete(self, account_id: str):
        raise NotImplementedError

    def get_user_accounts(self, user_id: str, bank_id: str) -> list:
        raise NotImplementedError

    def change_status(self, account_id: str, status: str):
        raise NotImplementedError

    def get_all_inactive(self, bank_id: str) -> list[Account]:
        raise NotImplementedError

    def _row_to_account(self, row) -> Account:
        raise NotImplementedError