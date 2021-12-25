import datetime
from logging import Logger
from rich.console import Console
from src.core.common_database_handling_statements import DB
from src.core.global_info import LOGS_DB_PATH, LOGS_DB_ROW_ONE, LOGS_DB_TABLE_NAME 

c = Console()

class Logging:
    """
    Created this class just bcoz i currently dont know how to log the log info to a file tho

    here is the COde :

    def __init__(self,log_statement="") -> None:
        self.log_statement = log_statement # ANd log statement to log
    
    def real_logging(self,db_name=LOGS_DB_PATH, table_name=LOGS_DB_TABLE_NAME ,row_data=LOGS_DB_ROW_ONE):
        :real_logging: 
            This function only saves the logs statements to `log DB `
            And DOES NOT OUTPUT log statements
        db = DB(db_name,table_name,row_data)
        data = {
                row_data[0] : f"{str(datetime.datetime.now())}",
                row_data[1] : self.log_statement
                }
        db.write(data)

    def log_to_term(self,db_name=LOGS_DB_PATH, table_name=LOGS_DB_TABLE_NAME ,row_data=LOGS_DB_ROW_ONE):
        :real_logging: 
            This function only saves the logs statements to `log DB `
            And DOES NOT OUTPUT log statements
        db = DB(db_name,table_name,row_data)
        data = {
                row_data[0] : f"{str(datetime.datetime.now())}",
                row_data[1] : self.log_statement
                }
        db.write(data)
        c.print(f"[ {c.get_datetime()} ]  {self.log_statement}",overflow="ellipsis")
    """
    def log(self,log_statement="",cout=False,db_name=LOGS_DB_PATH, table_name=LOGS_DB_TABLE_NAME ,row_data=LOGS_DB_ROW_ONE):
        """
        This is the main logger to save to the db or also output to the db
        log(self,cout=False | Bool)
        """
        db = DB(db_name,table_name,row_data)
        data = {
                row_data[0] : f"{str(datetime.datetime.now())}",
                row_data[1] : log_statement
                }
        
        db.write(data)
    
        if cout == True:
            c.print(f"[ {c.get_datetime()} ]  {log_statement}",overflow="ellipsis")


l = Logging()
for i in range(1,1001):
    l.log(log_statement=f"At Epoch :: {i}",cout=True)
