import sqlite3
from typing import Dict

class DB:
    """
    Got an new approach towards this project and so this class will hold most or
    all necessary functions for the handling of data ...
    ___________________________________________________________________________
    NOTE :
        This will only have the common data handling functionalities
    ___________________________________________________________________________
    """
    def __init__(self,db_name,table_name,row_data) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.row_data = row_data

    def connect_to_database(self):
        pass

    def write(self,data):
        """
        Common statements :
            table creation => CREATE TABLE IF NOT EXISTS `table name` (`row1` type, `row2` type, ... 'rowx' type)
            insertion of data => INSERT INTO `table name` VALUES (?, ?, ?, ... ?)

        """
        database = sqlite3.connect(self.db_name)
        csr = database.cursor()
        create_table = f"CREATE TABLE IF NOT EXISTS {self.table_name} (  )"
        csr.execute(create_table)
