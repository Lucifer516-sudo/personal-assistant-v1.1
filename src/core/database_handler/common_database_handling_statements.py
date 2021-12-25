import sqlite3

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

        row_data_string = row_data_string.strip(", ")
        create_table = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({row_data_string})"
        qstion_marks = ""

        for _ in data:
            qstion_marks += "?, "

        qstion_marks = qstion_marks.strip(", ")
        insert_data = f"INSERT INTO {self.table_name} VALUES ({qstion_marks})"
        d = tuple(data.values())
        csr.execute(create_table)
        csr.execute(insert_data,tuple(data.values()))
        database.commit()
        database.close()
#        print("commit status : OK")

# d = DB("test.sqlite3","test_table_name",row_data=["row1","row2","row3"])
# data = {
#         "row1": "1",
#         "row2" : "2",
#         "row3" : "3"
#         }
# d.write(data)
