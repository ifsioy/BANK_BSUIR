from src.domain.entities.transaction import Transaction
from src.domain.interfaces.ITransactionRepository import ITransactionRepository
from src.infrastructure.db.db_connection import get_db_connection

class SQLiteTransactionRepository(ITransactionRepository):
    def get_all(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, from_id, to_id, amount, date FROM transactions
            ''')
            rows = cursor.fetchall()
            transactions = []
            for row in rows:
                transaction = Transaction(
                    from_id=row[1],
                    to_id=row[2],
                    amount=row[3],
                    date=row[4],
                    id=row[0]
                )
                transactions.append(transaction)
            return transactions

    def get_by_id(self, transaction_id: str):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, from_id, to_id, amount, date FROM transactions WHERE id = ?
            ''', (transaction_id,))
            row = cursor.fetchone()
            if row:
                return Transaction(
                    from_id=row[1],
                    to_id=row[2],
                    amount=row[3],
                    date=row[4],
                    id=row[0]
                )
            return None

    def add(self, transaction: Transaction):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO transactions (id, from_id, to_id, amount, date)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                transaction.id,
                transaction.from_id,
                transaction.to_id,
                transaction.amount,
                transaction.date
            ))
            conn.commit()