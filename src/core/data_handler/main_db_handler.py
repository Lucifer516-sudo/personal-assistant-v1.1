from src.core.global_info import MAIN_DB_PATH,MAIN_DB_TABLE_NAME,MAIN_DB_ROW_ONE
from src.core.configurer.directories_creator import make_the_home_dir_to_save_the_db
from loguru import logger as lgr
catch = lgr.catch

@catch
def add_account_details_to_main_db(account_name: str, date_created: str, path_located: str):
    # This function adds the data to the main db to get in the if needed
    make_the_home_dir_to_save_the_db()
    record_added = False
    import sqlite3
    db = sqlite3.connect(MAIN_DB_PATH)
    c = db.cursor()
    create_table_in_main_db = f"create table if not exists {MAIN_DB_TABLE_NAME} ({MAIN_DB_ROW_ONE[0]} text, {MAIN_DB_ROW_ONE[1]} text, {MAIN_DB_ROW_ONE[2]} text)"
    add_account_details_in_main_db = f"insert into {MAIN_DB_TABLE_NAME} values (?, ?, ?)"
    c.execute(create_table_in_main_db)
    c.execute(add_account_details_in_main_db,(account_name,date_created,path_located))
    db.commit()
    db.close()
    record_added = True
    return record_added


