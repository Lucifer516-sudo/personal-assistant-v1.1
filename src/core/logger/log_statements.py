"""
Boiler Plate Log Statement:
    On >> [class: ClassName] :: ClassName.MethodName << FileName.py
"""
import datetime
from rich.console import Console
from ..database_handler.common_database_handling_statements import DB
from ..global_info import LOGS_DB_PATH, LOGS_DB_ROW_ONE, LOGS_DB_TABLE_NAME

c = Console()


class Logging:
    """
    Created this class just bcoz i currently dont know how to log the log info to a file tho
    """
    def __init__(self, cout) -> None:
        self.cout = cout

    def log(self, log_statement, log_level="INFO", db_name=LOGS_DB_PATH, table_name=LOGS_DB_TABLE_NAME, row_data=LOGS_DB_ROW_ONE):
        """
        This is the main logger to save to the db or also output to the db
        log(self,cout=False | Bool)
        :LOG_LEVELS:
            -> INFO
            -> DEBUG
            -> WARN
            -> CRITICAL
        """
        db = DB(db_name, table_name, row_data)
        data = {
                row_data[0]: f"{str(datetime.datetime.now())}",
                row_data[1]: log_statement,
                row_data[2]: log_level
                }

        db.write(data)

        if self.cout:
            c.print(f"[ {c.get_datetime()} ]  {log_statement}", overflow="ellipsis")

        return True


Logging(1).log("test")
