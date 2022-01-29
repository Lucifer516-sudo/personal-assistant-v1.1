from src.core.data_handler.hasher import Hash
from src.core.data_handler.render_text import Text
from src.core.global_info import ACCOUNT_DB_TABLE_NAME, ACCOUNTS_DB_PATH, ACCOUNT_DB_ROW_ONE, format_name, MAIN_DB_PATH, MAIN_DB_TABLE_NAME, MAIN_DB_ROW_ONE
from src.core.logger.log_statements import Logging
from src.core.database_handler.common_database_handling_statements import DB
import os
from datetime import datetime
from rich.traceback import install
install()


class Account:
    def __init__(self, user_name: str, user_email: str, user_dob: str, user_passwd: str) -> None:
        self.user_name = user_name
        self.user_email = user_email
        self.user_dob = user_dob
        self.user_passwd = user_passwd
        self.logger = Logging(cout=0)
        self.log = self.logger.log

    def check_for_an_account(self):
        DataBase = DB(MAIN_DB_PATH, MAIN_DB_TABLE_NAME, MAIN_DB_ROW_ONE)
        data = DataBase.search()
        account_exists = False
        for d in data:
            if d[0] == self.user_name:
                account_exists = True
        return account_exists

    def create_account(self):
        if not self.check_for_an_account():
            AC_NAME = format_name(self.user_name)
            ACCOUNTS_DB_PATH_ = f"{ACCOUNTS_DB_PATH}{os.path.sep}{AC_NAME}.db"
            #  Writing data to the main data base
            self.log("Got connected to the Main Database")
            DataBaseMain = DB(MAIN_DB_PATH, MAIN_DB_TABLE_NAME, MAIN_DB_ROW_ONE)
            DataBase = DB(ACCOUNTS_DB_PATH_, ACCOUNT_DB_TABLE_NAME, ACCOUNT_DB_ROW_ONE)
            hexhash = Hash(bytes(self.user_passwd, encoding='utf-8')).hash()
            data = {
                    ACCOUNT_DB_ROW_ONE[0]: self.user_name,
                    ACCOUNT_DB_ROW_ONE[1]: self.user_email,
                    ACCOUNT_DB_ROW_ONE[2]: self.user_dob,
                    ACCOUNT_DB_ROW_ONE[3]: hexhash,
                    }
            self.log(f"Writing data: {self.user_name}, {self.user_email}, {self.user_dob}, {Text(self.user_passwd).censor()}")
            DataBase.write(data, )
            del DataBase
            data_main = {
                     MAIN_DB_ROW_ONE[0]: self.user_name,
                     MAIN_DB_ROW_ONE[2]: str(datetime.now()),
                     MAIN_DB_ROW_ONE[3]: ACCOUNTS_DB_PATH_,
                     MAIN_DB_ROW_ONE[4]: hexhash,
                     }
            DataBaseMain.write(data_main)
            return True
        else:
            return False


name = "Test Name"
email = "test@gmail.com"
dob = "02-09-2005"
passwd = 'passwd'
Account(name, email, dob, passwd).create_account()
print(Text(name).censor())
