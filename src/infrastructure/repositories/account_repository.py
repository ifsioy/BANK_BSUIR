from src.domain.entities.account import Account
from src.domain.interfaces.IAccountRepository import IAccountRepository
from src.infrastructure.db.db_connection import get_db_connection


class SQLiteAccountRepository(IAccountRepository):
    def add(self, account):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO accounts (id, user_id, balance, bank_id)
                VALUES (?, ?, ?, ?)
            ''', (
                account.id,
                account.user_id,
                account.balance,
                account.bank_id
            ))
            conn.commit()

    def get_by_id(self, account_id: str):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, user_id, balance, bank_id FROM accounts WHERE id = ?
            ''', (account_id,))
            row = cursor.fetchone()
            if row:
                return Account(
                    user_id=row[1],
                    balance=row[2],
                    bank_id=row[3],
                    id=row[0]
                )
            return None

    def update(account):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE accounts
                SET user_id = ?, balance = ?, bank_id = ?
                WHERE id = ?
            ''', (
                account.user_id,
                account.balance,
                account.bank_id,
                account.id
            ))
            conn.commit()

    def delete(self, account_id: str):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM accounts WHERE id = ?
            ''', (account_id,))
            conn.commit()