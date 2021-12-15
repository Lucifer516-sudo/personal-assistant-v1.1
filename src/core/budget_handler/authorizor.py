from src.core.global_info import MAIN_DB_PATH
def check_password_to_update_account(db_path: str, name: str, passwd: str):
    import sqlite3

    correct_passwd = False
    db_main = sqlite3.connect(MAIN_DB_PATH)
    c_main = db_main.cursor()
    c_main.execute("select * from ")
