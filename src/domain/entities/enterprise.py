import uuid

from src.domain.enums import EnterpriseType

class Enterprise:
    def __init__(self, enterprise_type: EnterpriseType, legal_name: str, unp: str, bank_bic: str, legal_address: str, id = None):
        self.id = id if id else str(uuid.uuid4())
        self.enterprise_type = enterprise_type
        self.legal_name = legal_name
        self.unp = unp
        self.bank_bic = bank_bic
        self.legal_address = legal_address

    def __str__(self):
        return (f"Enterprise(id={self.id}, "
                f"Enterprise(type={self.enterprise_type.value}, "
                f"legal_name={self.legal_name}, "
                f"unp={self.unp}, "
                f"bank_bic={self.bank_bic}, "
                f"legal_address={self.legal_address})")