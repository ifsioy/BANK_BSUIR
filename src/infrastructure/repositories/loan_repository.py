from src.domain.entities.loan import Loan
from src.domain.interfaces.ILoanRepository import ILoanRepository
from src.infrastructure.db.db_connection import get_db_connection


class SQLiteLoanRepository(ILoanRepository):
    def get_by_id(self, loan_id: str) -> Loan:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, term, interest_rate, user_id FROM loans WHERE id = ?
            ''', (loan_id,))
            row = cursor.fetchone()
            if row:
                return Loan(term=row[1], interest_rate=row[2], user_id=row[3], id=row[0])
            return None

    def add(self, loan: Loan):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO loans (id, term, interest_rate, user_id)
                VALUES (?, ?, ?, ?)
            ''', (
                loan.id,
                loan.term,
                loan.interest_rate,
                loan.user_id
            ))
            conn.commit()