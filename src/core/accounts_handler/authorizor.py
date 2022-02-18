from src.core.accounts_handler.main_db_handler import MainDB
class Login:
    def __init__(self, user_name: str, user_passwd: bytes) -> None:
        self.user_name = user_name
        self.user_passwd = user_passwd

    def authorize(self,passwd_hash_ipt):
        ...
