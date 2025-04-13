from src.domain.entities.enterprise import Enterprise
from src.domain.interfaces.IEnterpriseRepository import IEnterpriseRepository
from src.infrastructure.db.db_connection import get_db_connection


class SQLiteEnterpriseRepository(IEnterpriseRepository):
    def get_by_id(self, enterprise_id: str):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, type, legal_name, unp, bank_bic, legal_address FROM enterprises WHERE id = ?
            ''', (enterprise_id,))
            row = cursor.fetchone()
            if row:
                return Enterprise(
                    enterprise_type=row[1],
                    legal_name=row[2],
                    unp=row[3],
                    bank_bic=row[4],
                    legal_address=row[5],
                    id=row[0]
                )
            return None

    def add(self, enterprise: Enterprise):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO enterprises (id, type, legal_name, unp, bank_bic, legal_address)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                enterprise.id,
                enterprise.enterprise_type,
                enterprise.legal_name,
                enterprise.unp,
                enterprise.bank_bic,
                enterprise.legal_address
            ))
            conn.commit()

    def update(self, enterprise: Enterprise):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE enterprises
                SET type = ?, legal_name = ?, unp = ?, bank_bic = ?, legal_address = ?
                WHERE id = ?
            ''', (
                enterprise.enterprise_type,
                enterprise.legal_name,
                enterprise.unp,
                enterprise.bank_bic,
                enterprise.legal_address,
                enterprise.id
            ))
            conn.commit()

    def delete(self, enterprise_id: str):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM enterprises WHERE id = ?
            ''', (enterprise_id,))
            conn.commit()