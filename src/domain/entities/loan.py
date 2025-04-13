import uuid

class Loan:
    def __init__(self, term: int, interest_rate: float, user_id: str, id = None):
        if term <= 0:
            raise ValueError("Loan term must be a positive value.")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")

        self.id = id if id else str(uuid.uuid4())
        self.term = term
        self.interest_rate = interest_rate
        self.user_id = user_id

    def __str__(self):
        return (f"Loan(id={self.id}, "
                f"term={self.term}, "
                f"interest_rate={self.interest_rate}, "
                f"user={self.user_id})")