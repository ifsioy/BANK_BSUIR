from src.domain.entities.user import User


class IUserRepository:
    def get_all(self):
        raise NotImplementedError

    def get_by_id(self, user_id: str):
        raise NotImplementedError

    def add(self, user: User):
        raise NotImplementedError

    def update(self, user: User):
        raise NotImplementedError

    def delete(self, user_id: str):
        raise NotImplementedError