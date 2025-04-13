from enum import Enum

class Role(Enum):
    CLIENT = "Client"
    OPERATOR = "Operator"
    MANAGER = "Manager"
    ADMIN = "Admin"
    EXTERNAL_SPECIALIST = "External Specialist"

class EnterpriseType(Enum):
    IP = "ИП"
    OOO = "ООО"
    ZAO = "ЗАО"
    PAO = "ПАО"

class Status(Enum):
    ACTIVE = "Active"
    FROZEN = "Frozen"
    CLOSED = "Closed"
    PENDING = "Pending"
    BLOCKED = "Blocked"
