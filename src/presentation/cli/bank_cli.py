from typing import List, Optional

from src.application.services.bank_service import BankService
from src.domain.entities.bank import Bank
from src.domain.entities.user import User
from src.domain.enums import Role
from src.presentation.cli.account_cli import AccountCLI


class BankCLI:
    def __init__(self):
        self.bank_service = BankService()
        self.account_cli = AccountCLI()
        self.selected_bank: Optional[Bank] = None

    def show_bank_menu(self, user: User):
        while True:
            if not user:
                return

            menu_items = [
                ("Список моих банков", self._show_user_banks),
                ("Список всех банков", self._show_all_banks),
                ("Добавить банк пользователю", self._add_bank_flow),
                ("Выбрать банк", self._select_bank_flow)
            ]

            if Role.ADMIN in user.roles:
                menu_items += [
                    ("Добавить банк в систему", self._create_bank_flow),
                    ("Удалить банк", self._delete_bank_flow),
                ]

            menu_items += [
                ("Вернуться", None)
            ]

            print("\n=== Управление банками ===")
            for i, (label, _) in enumerate(menu_items, 1):
                print(f"{i}. {label}")


            choice = input("Выберите действие: ").strip()

            try:
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(menu_items):
                    _, action = menu_items[choice_idx]

                    if action is None:
                        return

                    if action == self._show_user_banks:
                        self._show_user_banks(user.id)
                    elif action == self._show_all_banks:
                        self._show_all_banks()
                    elif action == self._add_bank_flow:
                        self._add_bank_flow(user.id)
                    elif action == self._create_bank_flow:
                        self._create_bank_flow(user)
                    elif action == self._delete_bank_flow:
                        self._delete_bank_flow(user)
                    elif action == self._select_bank_flow:
                        self._select_bank_flow(user)
                else:
                    print("Неверный выбор")

            except Exception as e:
                print(f"Ошибка: {e}")

    def _show_user_banks(self, user_id: str):
        banks = self.bank_service.get_user_banks(user_id)
        if not banks:
            print("У вас нет привязанных банков")
            return

        print("\nВаши банки:")
        for bank in banks:
            print(f"ID: {bank.id} | Название: {bank.name} | BIC: {bank.bic}")

    def _add_bank_flow(self, user_id: str):
        bank_id = input("Введите ID банка для добавления: ").strip()
        self.bank_service.add_bank_to_user(user_id, bank_id)
        print("Банк успешно добавлен")

    def _remove_bank_flow(self, user_id: str):
        bank_id = input("Введите ID банка для удаления: ").strip()
        self.bank_service.remove_bank_from_user(user_id, bank_id)
        print("Банк успешно удален")

    def _select_bank_flow(self, user: User):
        banks = self.bank_service.get_user_banks(user.id)
        if not banks:
            print("У вас нет привязанных банков")
            return

        print("\nДоступные банки:")
        for idx, bank in enumerate(banks, 1):
            print(f"{idx}. {bank.name} ({bank.bic})")

        choice = input("Выберите банк (номер): ").strip()
        try:
            index = int(choice) - 1
            if index < 0 or index >= len(banks):
                raise IndexError("Неверный индекс")

            self.selected_bank = banks[index]
            print(f"Выбран банк: {self.selected_bank.name}")

            self.account_cli.show_account_menu(user, self.selected_bank.id)

        except (ValueError, IndexError):
            print("Неверный выбор")

    def _show_all_banks(self):
        banks = self.bank_service.get_all_banks()
        if not banks:
            print("В системе нет банков")
            return

        print("\nВсе банки в системе:")
        for bank in banks:
            print(f"ID: {bank.id} | Название: {bank.name} | BIC: {bank.bic}")

    def _create_bank_flow(self, user: User):
        name = input("Введите название банка: ").strip()
        bic = input("Введите BIC банка: ").strip()

        new_bank = self.bank_service.create_bank(user, name, bic)
        print(f"Банк {new_bank.name} успешно создан!")

    def _delete_bank_flow(self, user: User):
        bank_id = input("Введите ID банка для удаления: ").strip()
        self.bank_service.delete_bank(user, bank_id)
        print("Банк успешно удален")