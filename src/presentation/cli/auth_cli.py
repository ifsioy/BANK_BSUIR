from src.application.services.auth_service import AuthService
from src.presentation.cli.input_helper import UserInputHandler


class AuthCLI:
    def show_auth_menu(self):
        auth_service = AuthService()
        while True:
            print("\n=== Банковская система ===")
            print("1. Регистрация")
            print("2. Вход")
            print("3. Выход")
            choice = input("Выберите действие: ").strip()

            if choice == "1":
                user_data = UserInputHandler.get_user_input()
                UserInputHandler.validate_input(user_data)
                auth_service.register_user(user_data)
            elif choice == "2":
                user_data = UserInputHandler.get_login_user_input()
                UserInputHandler.validate_input(user_data)
                auth_service.login_user(user_data)
            elif choice == "3":
                print("До свидания!")
                exit()
            else:
                print("Неверный выбор, попробуйте снова")