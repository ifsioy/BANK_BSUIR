from src.domain.validators.validator import PassportValidator, PhoneValidator, EmailValidator, PasswordValidator


class UserInputHandler:
    @staticmethod
    def get_user_input():
        print('--- Регистрация нового пользователя ---')
        data = {
            "full_name": input("Введите ФИО: ").strip(),
            "passport": input("Введите серию и номер паспорта (AB1234567): ").strip(),
            "phone": input("Введите телефон (+375291234567): ").strip(),
            "email": input("Введите email: ").strip(),
            "id": input("Введите id: ").strip(),
            "password": input("Пароль: ").strip(),
            "confirm_password": input("Подтвердите пароль: ").strip()
        }
        return data

    @staticmethod
    def get_login_user_input():
        data = {
            "id": input("Введите id: ").strip(),
            "password": input("Пароль: ").strip()
        }
        return data

    @staticmethod
    def validate_input(data: dict) -> dict:
        errors = []

        if pwd_errors := PasswordValidator.validate(data["password"]):
            raise ValueError("\n".join(pwd_errors))

        if "full_name" in data and len(data["full_name"].split()) < 2:
            errors.append("ФИО должно содержать минимум 2 слова")

        if "passport" in data and not PassportValidator.validate(data["passport"]):
            errors.append("Неверный формат паспорта")

        if "phone" in data and not PhoneValidator.validate(data["phone"]):
            errors.append("Неверный формат телефона")

        if "email" in data and not EmailValidator.validate(data["email"]):
            errors.append("Неверный формат email")

        if errors:
            raise ValueError("\n".join(errors))

        return data