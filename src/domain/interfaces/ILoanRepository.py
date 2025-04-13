from src.domain.entities.loan import Loan


class ILoanRepository:
    def get_by_id(self, loan_id: str):
        raise NotImplementedError

    def add(self, loan: Loan):
        raise NotImplementedError