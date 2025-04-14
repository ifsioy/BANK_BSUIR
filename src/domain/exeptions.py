from src.logger import logger


class UserAlreadyExists(Exception):
    def __init__(self, message="User already exists."):
        logger.error(message)
        self.message = message
        super().__init__(self.message)

class PermissionDeniedError(Exception):
    def __init__(self, message="Permission denied."):
        logger.error(message)
        self.message = message
        super().__init__(self.message)

class AccountFrozenError(Exception):
    def __init__(self, message="Operation not allowed - account is frozen."):
        logger.error(message)
        self.message = message
        super().__init__(self.message)

class TransactionNotFoundError(Exception):
    def __init__(self, message="Transaction not found."):
        logger.error(message)
        self.message = message
        super().__init__(self.message)