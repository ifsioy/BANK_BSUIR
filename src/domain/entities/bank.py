import uuid


class Bank:
    def __init__(self, name: str, bic: str, id = str(uuid.uuid4())):
        self.id = id
        self.name = name
        self.bic = bic

    def __str__(self):
        return (f"Bank(id={self.id}, "
                f"Bank(name={self.name}, "
                f"bic={self.bic})")
