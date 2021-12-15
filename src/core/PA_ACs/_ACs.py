"""
This File holds the class to create a account with all necessary configs
"""
from src.core.configurer.directories_creator import make_the_home_dir_to_save_the_db
from src.core.budget_handler.account_creator import create_account


class Account:
    make_the_home_dir_to_save_the_db()
    def __init__(self,user_name, user_email, user_dob, user_passwd) -> None:
        self.user_name = user_name
        self.user_email = user_email
        self.user_dob = user_dob
        self.user_passwd = user_passwd

    def _create_account(self):
        # Creates the Account and returns the status
       ac_created = create_account(self.user_name, self.user_email, self.user_dob, self.user_passwd)
       return ac_created


