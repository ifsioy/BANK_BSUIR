from src.domain.enums import Role

class User:
    full_name: str
    passport: str
    id: str
    phone: str
    email: str
    roles: list[Role]

    def __init__(self, full_name: str, passport: str, id: str, phone: str, email: str, roles: list[Role]):
        self.full_name = full_name
        self.passport = passport
        self.id = id
        self.phone = phone
        self.email = email
        self.roles = roles


    def has_role(self, role: Role) -> bool:
        return role in self.roles


    def __str__(self):
        return (f"User({self.full_name}, "
                f"{self.passport}, "
                f"{self.id}, "
                f"{self.phone}, "
                f"{self.email}, "
                f"{self.roles})")