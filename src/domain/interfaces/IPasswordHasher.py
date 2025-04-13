
class IPasswordHasher:
    def hash(self, password: str) -> str:
        raise NotImplementedError

    def verify(self, password: str, hashed: str) -> bool:
        raise NotImplementedError