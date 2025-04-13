from src.domain.entities.bank import Bank


class IBankRepository:
    def get_by_id(self, bank_id: str):
        raise NotImplementedError("Method not implemented.")

    def add(self, bank: Bank):
        raise NotImplementedError("Method not implemented.")

    def update(self, bank: Bank):
        raise NotImplementedError("Method not implemented.")

    def delete(self, bank_id: str):
        raise NotImplementedError("Method not implemented.")

