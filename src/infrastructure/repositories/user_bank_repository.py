from src.domain.entities.bank import Bank
from src.domain.interfaces.IUserBankRepository import IUserBankRepository
from src.infrastructure.db.db_connection import get_db_connection


class SQLiteUserBankRepository(IUserBankRepository):
    def get_user_banks(self, user_id: str) -> list:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                            SELECT bank_id FROM user_banks WHERE user_id = ?
                        ''', (user_id,))
            bank_ids = [row['bank_id'] for row in cursor.fetchall()]

            if not bank_ids:
                return []

            cursor.execute(f'''
                            SELECT id, name, bic FROM banks WHERE id IN ({','.join(['?'] * len(bank_ids))})
                        ''', bank_ids)
            banks = cursor.fetchall()

            return [Bank(id=row['id'], name=row['name'], bic=row['bic']) for row in banks]

    def add_user_bank(self, user_id: str, bank_id: str):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                            INSERT INTO user_banks (user_id, bank_id) VALUES (?, ?)
                        ''', (user_id, bank_id))
            conn.commit()

    def delete_user_bank(self, user_id: str, bank_id: str):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                            DELETE FROM user_banks WHERE user_id = ? AND bank_id = ?
                        ''', (user_id, bank_id))
            conn.commit()