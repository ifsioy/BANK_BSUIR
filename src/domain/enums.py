from enum import Enum

class Role(Enum):
    CLIENT = "Client"
    OPERATOR = "Operator"
    MANAGER = "Manager"
    EXTERNAL_SPECIALIST = "External Specialist"
    ADMIN = "Admin"

class EnterpriseType(Enum):
    IP = "ИП"
    OOO = "ООО"
    ZAO = "ЗАО"
    PAO = "ПАО"