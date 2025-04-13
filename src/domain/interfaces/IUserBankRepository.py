
class IUserBankRepository:
    def get_user_banks(self, user_id: str) -> list:
        raise NotImplementedError

    def add_user_bank(self, user_id: str, bank_id: str):
        raise NotImplementedError

    def delete_user_bank(self, user_id: str, bank_id: str):
        raise NotImplementedError