
class ITransactionValidator:
    @staticmethod
    def validate_deposit(amount):
        raise NotImplementedError("Must implement validate_deposit method")

    @staticmethod
    def validate_withdrawal(account, amount):
        raise NotImplementedError("Must implement validate_withdrawal method")

    @staticmethod
    def validate_transfer(from_account, to_account, amount):
        raise NotImplementedError("Must implement validate_transfer method")