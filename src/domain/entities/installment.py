from src.domain.entities.user import User

class Installment:
    def __init__(self, installment_id: str, term: int, interest_rate: float, user: User, total_amount: float):
        if term <= 0:
            raise ValueError("Installment term must be a positive value.")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative.")

        self.installment_id = installment_id
        self.term = term
        self.interest_rate = interest_rate
        self.user = user
        self.total_amount = total_amount

    def __str__(self):
        return (f"Installment(id={self.installment_id}, "
                f"term={self.term}, "
                f"interest_rate={self.interest_rate}, "
                f"user={self.user.full_name}, "
                f"total_amount={self.total_amount})")