from src.domain.entities.transaction import Transaction


class ITransactionRepository:
    def get_all(self):
        raise NotImplementedError

    def get_by_id(self, transaction_id: str):
        raise NotImplementedError

    def get_by_account_id(self, account_id: str):
        raise NotImplementedError

    def add(self, transaction: Transaction):
        raise NotImplementedError