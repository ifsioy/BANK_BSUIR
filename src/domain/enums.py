from enum import Enum

class Role(Enum):
    CLIENT = "Client"
    MANAGER = "Manager"
    ADMIN = "Admin"
    OPERATOR = "Operator"
    EXTERNAL_SPECIALIST = "External Specialist"