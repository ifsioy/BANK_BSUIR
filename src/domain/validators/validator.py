import re

class EmailValidator:
    @staticmethod
    def validate(email: str) -> bool:
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

class PhoneValidator:
    @staticmethod
    def validate(phone: str) -> bool:
        pattern = r"^\+375(25|29|33|44)\d{7}$"
        return re.match(pattern, phone) is not None

class PassportValidator:
    @staticmethod
    def validate(passport: str) -> bool:
        pattern = r"^[A-Z]{2}\d{7}$"
        return re.match(pattern, passport) is not None

class PasswordValidator:
    @staticmethod
    def validate(password: str) -> list[str]:
        errors = []
        # if len(password) < 8:
        #     errors.append("Пароль должен содержать минимум 8 символов")
        if not re.search(r"\d", password):
            errors.append("Пароль должен содержать цифру")
        # if not re.search(r"[A-Z]", password):
        #     errors.append("Пароль должен содержать заглавную букву")
        # if not re.search(r"[!@#$%^&*]", password):
        #     errors.append("Пароль должен содержать спецсимвол (!@#$%^&*)")
        return errors