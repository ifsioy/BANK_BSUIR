from src.application.services.account_service import AccountService
from src.application.services.transaction_service import TransactionService
from src.domain.entities.account import Account
from typing import Optional

from src.domain.entities.user import User
from src.domain.enums import Role, Status
from src.domain.exeptions import PermissionDeniedError
from src.presentation.cli.account_operation_cli import AccountOperationCLI


class AccountCLI:
    def __init__(self):
        self.account_service = AccountService()
        self.transaction_service = TransactionService()
        self.selected_account: Optional[Account] = None

    def show_account_menu(self, user: User, bank_id: str):
        while True:
            if not user:
                return

            menu_items = [
                ("Список счетов", self._show_accounts),
                ("Создать новый счет", self._create_account_flow),
                ("Удалить счет", self._delete_account_flow),
                ("Выбрать счет", self._select_account_flow)
            ]

            if Role.MANAGER in user.roles or Role.ADMIN in user.roles:
                menu_items += [
                    ("Показать неактивные счета", self._show_inactive_accounts),
                    ("Заморозить счет", self._freeze_account_flow),
                    ("Разморозить счет", self._unfreeze_account_flow),
                    ("Активировать счет", self._activate_account_flow),
                    ("Показать все транзакции", self._show_all_transactions),
                    ("Отменить транзакцию", self._reverse_transaction_flow),
                ]

            menu_items.append(("Вернуться к выбору банка", None))

            print("\n=== Управление счетами ===")
            for i, (label, _) in enumerate(menu_items, 1):
                print(f"{i}. {label}")

            choice = input("Выберите действие: ").strip()

            try:
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(menu_items):
                    _, action = menu_items[choice_idx]

                    if action is None:
                        return

                    # Вызываем соответствующий метод с параметрами
                    if action == self._show_accounts:
                        self._show_accounts(user.id, bank_id)
                    elif action == self._create_account_flow:
                        self._create_account_flow(user.id, bank_id)
                    elif action == self._delete_account_flow:
                        self._delete_account_flow()
                    elif action == self._select_account_flow:
                        self._select_account_flow(user.id, bank_id)
                    elif action == self._freeze_account_flow:
                        self._freeze_account_flow(user.id)
                    elif action == self._unfreeze_account_flow:
                        self._unfreeze_account_flow(user.id)
                    elif action == self._show_inactive_accounts:
                        self._show_inactive_accounts(bank_id)
                    elif action == self._activate_account_flow:
                        self._activate_account_flow(user.id)
                    elif action == self._show_all_transactions:
                        self._show_all_transactions()
                    elif action == self._reverse_transaction_flow:
                        self._reverse_transaction_flow()
                else:
                    print("Неверный выбор")

            except ValueError as e:
                print("Ошибка: ", e)
            except Exception as e:
                print(f"Ошибка: {str(e)}")

    def _show_accounts(self, user_id: str, bank_id: str):
        accounts = self.account_service.get_user_accounts(user_id, bank_id)
        if not accounts:
            print("У вас нет счетов в этом банке")
            return

        print("\nВаши счета:")
        for acc in accounts:
            print(f"ID: {acc.id} | Баланс: {acc.balance:.2f} | Статус: {acc.status}")

    def _create_account_flow(self, user_id: str, bank_id: str):
        try:
            balance = float(input("Начальный баланс: "))
            account = self.account_service.create_account(user_id, bank_id, balance)
            print(f"Счет {account.id} создан. Текущий баланс: {account.balance:.2f}")
        except ValueError:
            print("Некорректная сумма")

    def _delete_account_flow(self):
        account_id = input("Введите ID счета для удаления: ").strip()
        self.account_service.delete_account(account_id)
        print("Счет успешно удален")

    def _select_account_flow(self, user_id: str, bank_id: str) -> bool:
        accounts = self.account_service.get_user_accounts(user_id, bank_id)
        if not accounts:
            return False

        print("\nДоступные счета:")
        for idx, acc in enumerate(accounts, 1):
            print(f"{idx}. Счет {acc.id} ({acc.balance:.2f})")

        choice = input("Выберите счет (номер): ").strip()
        try:
            index = int(choice) - 1
            if index < 0 or index >= len(accounts):
                raise IndexError
            if accounts[index].status != Status.ACTIVE.value:
                raise Exception("Счет неактивен")
            self.selected_account = accounts[index]
            print(f"Выбран счет: {self.selected_account.id}")

            AccountOperationCLI().show_operations_menu(user_id, accounts[index])

            return True
        except (ValueError, IndexError):
            print("Неверный выбор")
            return False

    def _freeze_account_flow(self, user_id):
        account_id = input("Введите ID счета для блокировки: ").strip()
        self.account_service.set_status(user_id, account_id, Status.FROZEN)
        print(f"Счет {account_id} успешно заблокирован")

    def _unfreeze_account_flow(self, user_id):
        account_id = input("Введите ID счета для разблокировки: ").strip()
        self.account_service.set_status(user_id, account_id, Status.ACTIVE)
        print(f"Счет {account_id} успешно разблокирован")

    def _show_inactive_accounts(self, bank_id: str):
        accounts = self.account_service.get_inactive_accounts(bank_id)
        if not accounts:
            print("Нет неактивных счетов")
            return

        print("\nНеактивные счета:")
        for acc in accounts:
            print(f"ID: {acc.id} | Баланс: {acc.balance} | Статус: {acc.status}")

    def _activate_account_flow(self, user_id: str):
        account_id = input("Введите ID счета для активации: ").strip()
        try:
            self.account_service.set_status(user_id, account_id, Status.ACTIVE)
            print("Счет успешно активирован")
        except PermissionDeniedError as e:
            print(f"Ошибка доступа: {str(e)}")
        except ValueError as e:
            print(f"Ошибка: {str(e)}")

    def _show_all_transactions(self):
        transactions = self.transaction_service.get_all()
        if not transactions:
            print("Нет транзакций для этого счета")
            return

        print("\nВсе транзакции:")
        for transaction in transactions:
            print(f"ID: {transaction.id} | Сумма: {transaction.amount} | Дата: {transaction.date}"
                  f" | FROM: {transaction.from_id} | TO: {transaction.to_id} | ")

    def _reverse_transaction_flow(self):
        transaction_id = input("Введите ID транзакции для отмены: ").strip()
        try:
            self.transaction_service.reverse_transaction(transaction_id)
            print("Транзакция успешно отменена")
        except ValueError as e:
            print(f"Ошибка: {str(e)}")
