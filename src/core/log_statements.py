import datetime

from rich.console import Console
from rich.traceback import install
install(show_locals=True)
c = Console()
from src.core.global_info import (
    LOGS_DB_NAME,
    LOGS_DB_PATH,
    LOGS_DB_ROW_ONE,
    LOGS_DB_TABLE_NAME,
)
from src.core.common_database_handling_statements import DB

class Logging:
    """
    Created this class just bcoz i currently dont know how to log the log info to a file tho
    """
    def __init__(self,log_statement="") -> None:
        self.log_statement = log_statement # ANd log statement to log

    def real_logging(self,db_name=LOGS_DB_PATH, table_name=LOGS_DB_TABLE_NAME ,row_data=LOGS_DB_ROW_ONE):
        db = DB(db_name,table_name,row_data)
        data = {
                row_data[0] : f"{str(datetime.datetime.now())}",
                row_data[1] : self.log_statement
                }
        db.write(data)

    def log(self,cout=False):
        if cout != True:
            pass
        if cout == True:
            pass


c.log(log_locals=True)

l = Logging("Test")

for i in range(10):
    l.real_logging(db_name=LOGS_DB_PATH)

