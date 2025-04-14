from src.domain.entities.account import Account
from src.domain.entities.user import User
from src.application.services.account_operation_service import AccountOperationService
from src.logger import logger


class AccountOperationCLI:
    account: Account
    user_id: str
    def __init__(self):
        self.operation_service = AccountOperationService()

    def show_operations_menu(self, user_id, account):
        self.account = account
        self.user_id = user_id
        while True:
            print(f"\n=== Операции со счетом {self.account.id} ===")
            print(f"Текущий баланс: {self.account.balance:.2f}")
            print("1. Пополнить счет")
            print("2. Снять наличные")
            print("3. Перевести на другой счет")
            print("4. История операций")
            print("5. Вернуться назад")

            choice = input("Выберите действие: ").strip()

            try:
                if choice == "1":
                    self._deposit_flow()
                elif choice == "2":
                    self._withdraw_flow()
                elif choice == "3":
                    self._transfer_flow()
                elif choice == "4":
                    self._show_transaction_history()
                elif choice == "5":
                    return
                else:
                    print("Неверный выбор")
            except ValueError as e:
                logger.error(e)
                print(f"Ошибка: {str(e)}")
            except Exception as e:
                logger.error(e)
                print(f"Произошла ошибка: {str(e)}")

    def _deposit_flow(self):
        amount = float(input("Введите сумму для пополнения: "))
        self.operation_service.deposit(self.account.id, amount)
        self.account = self.operation_service.get_updated_account(self.account.id)
        print(f"Счет пополнен. Новый баланс: {self.account.balance:.2f}")

    def _withdraw_flow(self):
        amount = float(input("Введите сумму для снятия: "))
        self.operation_service.withdraw(self.account.id, amount)
        self.account = self.operation_service.get_updated_account(self.account.id)
        print(f"Средства сняты. Новый баланс: {self.account.balance:.2f}")

    def _transfer_flow(self):
        to_account_id = input("Введите ID счета получателя: ").strip()
        amount = float(input("Введите сумму для перевода: "))

        self.operation_service.transfer(
            from_account_id=self.account.id,
            to_account_id=to_account_id,
            amount=amount
        )
        self.account = self.operation_service.get_updated_account(self.account.id)
        print(f"Перевод выполнен. Новый баланс: {self.account.balance:.2f}")

    def _show_transaction_history(self):
        transactions = self.operation_service.get_transaction_history(self.account.id)
        if not transactions:
            print("История операций пуста")
            return

        print("\nПоследние операции:")
        for t in transactions:
            print(f"{t.date} | {t.to_id} | {t.amount:.2f}")