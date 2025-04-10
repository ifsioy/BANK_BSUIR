from domain.enums import Role

class Client:
    def __init__(self, full_name: str, passport_series_number: str, id_number: str, phone: str, email: str, is_foreign: bool = False, passport_country: str = None):
        self.full_name = full_name
        self.passport_series_number = passport_series_number
        self.id_number = id_number
        self.phone = phone
        self.email = email
        self.is_foreign = is_foreign
        self.passport_country = passport_country if is_foreign else None

    def __str__(self):
        return (f"Client(full_name={self.full_name},"
                f" passport_series_number={self.passport_series_number},"
                f" id_number={self.id_number},"
                f" phone={self.phone},"
                f" email={self.email},"
                f" is_foreign={self.is_foreign},"
                f" passport_country={self.passport_country})")