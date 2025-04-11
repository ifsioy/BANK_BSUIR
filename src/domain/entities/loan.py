from src.domain.entities.user import User

class Loan:
    def __init__(self, loan_id: str, term: int, interest_rate: float, user: User):
        if term <= 0:
            raise ValueError("Loan term must be a positive value.")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")

        self.loan_id = loan_id
        self.term = term
        self.interest_rate = interest_rate
        self.user = user

    def __str__(self):
        return (f"Loan(id={self.loan_id}, "
                f"term={self.term}, "
                f"interest_rate={self.interest_rate}, "
                f"user={self.user.full_name})")