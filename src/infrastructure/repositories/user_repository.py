from typing import List

from src.domain.entities.user import User
from src.domain.enums import Role
from src.domain.interfaces.IUserRepository import IUserRepository
from src.infrastructure.db.db_connection import get_db_connection


class SQLiteUserRepository(IUserRepository):
    def get_all(self) -> List[User]:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, password_hash, full_name, passport, phone, email FROM users
            ''')
            rows = cursor.fetchall()
            users = []
            for row in rows:
                user = User(
                    id=row[0],
                    password_hash=row[1],
                    full_name=row[2],
                    passport=row[3],
                    phone=row[4],
                    email=row[5],
                    roles=[]
                )
                cursor.execute('''
                                SELECT role_id FROM user_roles WHERE user_id = ?
                            ''', (user.id,))
                role_rows = cursor.fetchall()
                user.roles = [Role(role_row[0]) for role_row in role_rows]
                users.append(user)
            return users

    def get_by_id(self, user_id: str) -> User:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, password_hash, full_name, passport, phone, email FROM users WHERE id = ?
            ''', (user_id,))
            row = cursor.fetchone()

            # for column in row:
            #     print(column, type(column))

            if row:
                user = User(
                    id=row[0],
                    password_hash=row[1],
                    full_name=row[2],
                    passport=row[3],
                    phone=row[4],
                    email=row[5],
                    roles=[]
                )
                cursor.execute('''
                    SELECT role FROM user_roles WHERE user_id = ?
                ''', (user_id,))
                rows = cursor.fetchall()
                user.roles = [Role(role_row[0]) for role_row in rows]
                return user
            return None

    def add(self, user):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (id, password_hash, full_name, passport, phone, email)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                user.id,
                user.password_hash,
                user.full_name,
                user.passport,
                user.phone,
                user.email
            ))
            for role in user.roles:
                cursor.execute('''
                                    INSERT INTO user_roles (user_id, role)
                                    VALUES (?, ?)
                                ''', (user.id, role.value))
            conn.commit()

    def update(self, user):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE users
                SET password_hash = ?, full_name = ?, passport = ?, phone = ?, email = ?
                WHERE id = ?
            ''', (
                user.password_hash,
                user.full_name,
                user.passport,
                user.phone,
                user.email,
                user.id
            ))
            cursor.execute('''
                DELETE FROM user_roles WHERE user_id = ?
            ''', (user.id,))
            for role in user.roles:
                cursor.execute('''
                                    INSERT INTO user_roles (user_id, role)
                                    VALUES (?, ?)
                                ''', (user.id, role.value))
            conn.commit()

    def delete(self, user_id: str):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM users WHERE id = ?
            ''', (user_id,))
            cursor.execute('''
                DELETE FROM user_roles WHERE user_id = ?
            ''', (user_id,))
            conn.commit()
