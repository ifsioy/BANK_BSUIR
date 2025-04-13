

class IUserRoleRepository:
    def get_user_roles(self, user_id: str) -> list:
        raise NotImplementedError

    def add(self, user_id: str, role_id: str) -> None:
        raise NotImplementedError