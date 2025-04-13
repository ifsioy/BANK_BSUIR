from src.domain.entities.account import Account
from src.domain.enums import Status
from src.domain.interfaces.IAccountRepository import IAccountRepository
from src.infrastructure.db.db_connection import get_db_connection


class SQLiteAccountRepository(IAccountRepository):
    def add(self, account: Account):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO accounts (id, user_id, balance, bank_id, status)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                account.id,
                account.user_id,
                account.balance,
                account.bank_id,
                account.status
            ))
            conn.commit()
        return account

    def get_by_id(self, account_id: str):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, user_id, balance, bank_id, status FROM accounts WHERE id = ?
            ''', (account_id,))
            row = cursor.fetchone()
            if row:
                return Account(
                    user_id=row[1],
                    balance=row[2],
                    bank_id=row[3],
                    id=row[0],
                    status=row[4]
                )
            return None

    def update(self, account):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE accounts
                SET user_id = ?, balance = ?, bank_id = ?, status = ?
                WHERE id = ?
            ''', (
                account.user_id,
                account.balance,
                account.bank_id,
                account.status,
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

    def get_user_accounts(self, user_id: str, bank_id: str) -> list[Account]:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, user_id, balance, bank_id, status 
                FROM accounts 
                WHERE user_id = ? AND bank_id = ?
            ''', (user_id, bank_id))
            return [Account(**row) for row in cursor.fetchall()]

    def change_status(self, account_id: str, new_status: Status):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE accounts 
                SET status = ? 
                WHERE id = ?
            ''', (new_status.value, account_id))
            conn.commit()

    def get_all_inactive(self, bank_id: str) -> list[Account]:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, user_id, balance, bank_id, status 
                FROM accounts 
                WHERE status != ? AND bank_id = ?
            ''', (Status.ACTIVE.value, bank_id))
            return [self._row_to_account(row) for row in cursor.fetchall()]

    def _row_to_account(self, row) -> Account:
        return Account(
            id=row[0],
            user_id=row[1],
            balance=row[2],
            bank_id=row[3],
            status=row[4]
        )
