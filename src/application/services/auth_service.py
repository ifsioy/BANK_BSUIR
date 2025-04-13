from src.domain.entities.user import User
from src.domain.enums import Role
from src.domain.exeptions import UserAlreadyExists
from src.infrastructure.repositories.user_repository import SQLiteUserRepository
from src.infrastructure.security.password_hasher import BCryptPasswordHasher


class AuthService:
    def register_user(self, user_data: dict) -> User:

        if user_data["password"] != user_data["confirm_password"]:
            raise ValueError("Пароли не совпадают")

        user_repo = SQLiteUserRepository()
        if user_repo.get_by_id(user_data["id"]):
            raise UserAlreadyExists()

        hashed_password = BCryptPasswordHasher().hash(user_data["password"])

        new_user = User(
            id=user_data["id"],
            full_name=user_data["full_name"],
            passport=user_data["passport"],
            phone=user_data["phone"],
            email=user_data["email"],
            password_hash=hashed_password,
            roles=[Role.CLIENT],
        )

        user_repo.add(new_user)
        return new_user

    def login_user(self, user_data: dict) -> User:
        user_repo = SQLiteUserRepository()
        print(user_data["id"])
        print(type(user_data["id"]))

        user = user_repo.get_by_id(user_data["id"])

        if not user:
            raise ValueError("Пользователь не найден")

        print(user_data["password"],'-'*5, user.password_hash)

        if not BCryptPasswordHasher().verify(user_data["password"], user.password_hash):
            raise ValueError("Неверный пароль")

        return user
