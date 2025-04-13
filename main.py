from src.infrastructure.db.db_connection import init_db
from src.infrastructure.repositories.user_repository import SQLiteUserRepository
from src.presentation.cli.auth_cli import AuthCLI


def main():

    init_db()
    auth_cli = AuthCLI()

    auth_cli.show_auth_menu()

if __name__ == "__main__":
    main()