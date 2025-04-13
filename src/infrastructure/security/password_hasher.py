from passlib.context import CryptContext
from src.domain.interfaces.IPasswordHasher import IPasswordHasher


class BCryptPasswordHasher(IPasswordHasher):
    def __init__(self):
        self.ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash(self, password: str) -> str:
        return self.ctx.hash(password)

    def verify(self, password: str, hashed: str) -> bool:
        return self.ctx.verify(password, hashed)