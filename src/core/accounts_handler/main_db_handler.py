from src.core.global_info import MAIN_DB_PATH, MAIN_DB_TABLE_NAME, MAIN_DB_ROW_ONE
from src.core.database_handler.common_database_handling_statements import DB


class MainDB:
    def add_to_main_db(self):
        pass

    def update_main_db(self, data: dict):
        database = DB(MAIN_DB_PATH, MAIN_DB_TABLE_NAME, MAIN_DB_ROW_ONE)
        database.write(data)
