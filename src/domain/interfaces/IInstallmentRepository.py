from src.domain.entities.installment import Installment


class IInstallmentRepository:

    def get_by_id(self, installment_id: str):
        raise NotImplementedError

    def add(self, installment: dict):
        raise NotImplementedError

    def update(self, installment: Installment) -> None:
        raise NotImplementedError

    def delete(self, installment_id: str) -> None:
        raise NotImplementedError