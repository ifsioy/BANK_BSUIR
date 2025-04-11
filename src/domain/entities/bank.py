class Bank:
    def __init__(self, name: str, bic: str):
        self.name = name
        self.bic = bic

    def __str__(self):
        return (f"Bank(name={self.name}, "
                f"bic={self.bic})")
