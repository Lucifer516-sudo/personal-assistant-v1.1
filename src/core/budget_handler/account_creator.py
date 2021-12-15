import sqlite3
import datetime
import os
from loguru import logger as lgr
from src.core.global_info import ACCOUNTS_DB_PATH
catch = lgr.catch

@catch
def formatted_name(name: str):
    name = name +"__" + str(((str(datetime.datetime.now())).replace(":","~")).split(".")[0])
    return name

@catch
def check_for_account(name: str) -> bool:
    """
    check_for_account(name: str) -> bool
    --> checks if the account is there and returns the boolean value
    account_exists = False | BY DEFAULT |
    """
    account_exists = False
    accounts_in_ACCOUNTS_DB = os.listdir(ACCOUNTS_DB_PATH)
    accounts_in_ACCOUNTS_DB__Formatted = []

    for ac in accounts_in_ACCOUNTS_DB:
        accounts_in_ACCOUNTS_DB__Formatted.append(ac.split("__")[0])
    if name in accounts_in_ACCOUNTS_DB__Formatted:
        account_exists = True

    return account_exists
    
@catch
def create_account(name: str, email: str, dob: str, passwd: str):
    """ Create a/c if there is not one"""
    if not check_for_account(name):
        formatted_account_db_name = str(formatted_name(name))
        db = sqlite3.connect(f"{ACCOUNTS_DB_PATH}{os.path.sep}{formatted_account_db_name}.db")
        c = db.cursor()
        create_ac_table = "create table if not exists ACCOUNT_DETAILS (USER_NAME text, USER_EMAIL text, USER_DOB text, USER_PASSWD text)"
        c.execute(create_ac_table) # creating an a/c if not exists
        create_ac = "insert into ACCOUNT_DETAILS values (?, ?, ?, ?)"
        c.execute(create_ac,(name, email, dob, passwd))
        db.commit()
        db.close()
        print(f"Created the db file with name --> {formatted_account_db_name}\nCommit --> OK\nDB Closing --> OK")
@catch
def update_account(name, email, dob, passwd):  # Still development going on
    """Updates the account if exists"""
    # Checking if there is an account with the username
    formatted_account_db_name = str(str(name).upper()).replace(" ","_")
    db = sqlite3.connect(f"{ACCOUNTS_DB_PATH}{os.path.sep}{formatted_account_db_name}.db")
    c = db.cursor()
    update_ac = "update ACCOUNT_DETAILS set name = ?,"
    db.commit()
    db.close()
    print(f"Updated the db file with name --> {formatted_account_db_name}\nCommit --> OK\nDB Closing --> OK")





