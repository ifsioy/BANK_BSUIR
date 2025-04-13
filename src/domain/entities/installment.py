import uuid

class Installment:
    def __init__(self, term: int, interest_rate: float, user_id: str, total_amount: float, id = str(uuid.uuid4())):
        if term <= 0:
            raise ValueError("Installment term must be a positive value.")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative.")

        self.id = id
        self.term = term
        self.interest_rate = interest_rate
        self.user_id = user_id
        self.total_amount = total_amount

    def __str__(self):
        return (f"Installment(id={self.id}, "
                f"term={self.term}, "
                f"interest_rate={self.interest_rate}, "
                f"user={self.user_id}, "
                f"total_amount={self.total_amount})")