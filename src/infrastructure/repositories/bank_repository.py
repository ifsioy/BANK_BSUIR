from src.domain.entities.bank import Bank
from src.domain.interfaces.IBankRepository import IBankRepository
from src.infrastructure.db.db_connection import get_db_connection


class SQLiteBankRepository(IBankRepository):
    def get_all(self) -> list:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                            SELECT id, name, bic FROM banks
                        ''')
            rows = cursor.fetchall()
            return [Bank(id=row[0], name=row[1], bic=row[2]) for row in rows]

    def get_by_id(self, bank_id: str):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                            SELECT id, name, bic FROM banks WHERE id = ?
                        ''', (bank_id,))
            row = cursor.fetchone()
            if row:
                return Bank(name=row[1], bic=row[2], id=row[0])
            return None

    def add(self, bank):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                            INSERT INTO banks (id, name, bic)
                            VALUES (?, ?, ?)
                        ''', (
                bank.id,
                bank.name,
                bank.bic
            ))
            conn.commit()

    def update(self, bank):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                            UPDATE banks
                            SET name = ?, bic = ?
                            WHERE id = ?
                        ''', (
                bank.name,
                bank.bic,
                bank.id
            ))
            conn.commit()

    def delete(self, bank_id: str):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                            DELETE FROM banks WHERE id = ?
                        ''', (bank_id,))
            conn.commit()