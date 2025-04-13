import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent.parent / "data" / "financial.db"

def get_db_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        print("Connection to database established.")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    return conn

def init_db():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                full_name TEXT NOT NULL,
                passport TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_roles (
                user_id TEXT NOT NULL,
                role TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS banks (
                id TEXT PRIMARY KEY,
                bic TEXT PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                balance REAL NOT NULL,
                bank_id TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (bank_id) REFERENCES banks (id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS enterprises (
                id TEXT PRIMARY KEY,
                unp TEXT PRIMARY KEY,
                legal_name TEXT NOT NULL,
                bank_id TEXT NOT NULL,
                legal_address TEXT NOT NULL,
                enterprise_type TEXT NOT NULL,
                FOREIGN KEY (bank_id) REFERENCES banks (id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS loans (
                id TEXT PRIMARY KEY,
                term INTEGER NOT NULL,
                interest_rate REAL NOT NULL,
                user_id TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS installments (
                id TEXT PRIMARY KEY,
                term INTEGER NOT NULL,
                interest_rate REAL NOT NULL,
                user_id TEXT NOT NULL,
                total_amount REAL NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id TEXT PRIMARY KEY,
                from_id TEXT NOT NULL,
                to_id TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL,
                FOREIGN KEY (from_id) REFERENCES users (id)
                FOREIGN KEY (to_id) REFERENCES users (id)
            )
        ''')
        conn.commit()