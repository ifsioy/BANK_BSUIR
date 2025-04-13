from src.domain.entities.installment import Installment
from src.domain.interfaces.IInstallmentRepository import IInstallmentRepository
from src.infrastructure.db.db_connection import get_db_connection


class SQLiteInstallmentRepository(IInstallmentRepository):
    def get_by_id(self, installment_id: str):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM installments WHERE id = ?", (installment_id,))
            row = cursor.fetchone()
            if row:
                return Installment(
                    term=row[1],
                    interest_rate=row[2],
                    user_id=row[3],
                    total_amount=row[4],
                    id=row[0]
                )
            return None

    def add(self, installment: Installment) -> None:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO installments (id, term, interest_rate, user_id, total_amount)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                installment.id,
                installment.term,
                installment.interest_rate,
                installment.user_id,
                installment.total_amount
            ))
            conn.commit()

    def update(self, installment: Installment) -> None:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE installments
                SET term = ?, interest_rate = ?, user_id = ?, total_amount = ?
                WHERE id = ?
            ''', (
                installment.term,
                installment.interest_rate,
                installment.user_id,
                installment.total_amount,
                installment.id
            ))
            conn.commit()

    def delete(self, installment_id: str) -> None:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM installments WHERE id = ?
            ''', (installment_id,))
            conn.commit()


