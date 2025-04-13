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