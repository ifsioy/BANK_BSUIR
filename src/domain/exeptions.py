
class UserAlreadyExists(Exception):
    def __init__(self, message="User already exists."):
        self.message = message
        super().__init__(self.message)

class PermissionDeniedError(Exception):
    def __init__(self, message="Permission denied."):
        self.message = message
        super().__init__(self.message)

class AccountFrozenError(Exception):
    def __init__(self, message="Operation not allowed - account is frozen."):
        self.message = message
        super().__init__(self.message)

class TransactionNotFoundError(Exception):
    def __init__(self, message="Transaction not found."):
        self.message = message
        super().__init__(self.message)