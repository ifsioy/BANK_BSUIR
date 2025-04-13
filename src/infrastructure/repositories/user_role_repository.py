from src.domain.enums import Role
from src.domain.interfaces.IUserRoleRepository import IUserRoleRepository
from src.infrastructure.db.db_connection import get_db_connection


class SQLiteUserRoleRepository(IUserRoleRepository):
    def add(self, user_id: str, role: Role):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO user_roles (user_id, role)
                VALUES (?, ?)
            ''', (user_id, role))
            conn.commit()

    def get_user_roles(self, user_id: str) -> list:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT role FROM user_roles WHERE user_id = ?
            ''', (user_id,))
            rows = cursor.fetchall()
            return [row[0] for row in rows]


