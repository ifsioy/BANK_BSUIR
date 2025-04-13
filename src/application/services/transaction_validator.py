from src.domain.interfaces.ITransactionValidator import ITransactionValidator


class TransactionValidator(ITransactionValidator):
    @staticmethod
    def validate_deposit(amount):
        if amount <= 0:
            raise Exception("Сумма должна быть положительной")

    @staticmethod
    def validate_withdrawal(account, amount):
        if amount <= 0:
            raise Exception("Сумма должна быть положительной")
        if abs(account.balance - amount) > 1e-2:
            raise Exception()

    @staticmethod
    def validate_transfer(from_account, to_account, amount):
        if amount <= 0:
            raise Exception("Сумма должна быть положительной")
        if abs(from_account.balance - amount) > 1e-2:
            raise Exception()
        if from_account.id == to_account.id:
            raise Exception()