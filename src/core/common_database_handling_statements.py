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
    def __init__(self,db_name: str, table_name: str, row_data: list) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.row_data = row_data

    def write(self,data:dict):
        """
        Common statements :
            table creation => CREATE TABLE IF NOT EXISTS `table name` (`row1` type, `row2` type, ... 'rowx' type)
            insertion of data => INSERT INTO `table name` VALUES (?, ?, ?, ... ?)

        """
        database = sqlite3.connect(self.db_name)
        csr = database.cursor()
        row_data_string = ""
        for i in list(self.row_data):
            row_data_string += f"{i} text, "

        create_table = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({row_data_string})"
        qstion_marks = ""

        for _ in data:
            qstion_marks += "?, "

        insert_data = f"INSERT INTO {self.table_name} VALUES (qstion_marks)"
        csr.execute(create_table)
        csr.execute(insert_data,tuple(data.values()))
        database.commit()
        database.close()
