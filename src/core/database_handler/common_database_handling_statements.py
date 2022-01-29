import sqlite3


class DB:
    """
    Got an new approach towards this project and so this class will hold most or
    all necessary functions for the handling of data ...
    ___________________________________________________________________________
    NOTE :
        This will only have the common data handling functionalities
    ___________________________________________________________________________

    EXAMPLE CODE :
    -----------------------------------------------------------------------------
    | d = DB("test.sqlite3","test_table_name",row_data=["row1","row2","row3"])  |
    | data = {                                                                  |
    |         "row1": "1",                                                      |
    |         "row2" : "2",                                                     |
    |         "row3" : "3"                                                      |
    |         }                                                                 |
    | d.write(data)                                                             |
    -----------------------------------------------------------------------------
    """

    def __init__(self, db_name: str, table_name: str, row_data: list) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.row_data = row_data

    def create_table_if_not_exists(self):
        database = sqlite3.connect(self.db_name)
        csr = database.cursor()
        row_data_string = ""
        for _ in list(self.row_data):
            row_data_string += f"{_} text, "

        row_data_string = row_data_string.strip(", ")
        create_table = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({row_data_string})"
        csr.execute(create_table)
        database.commit()
        database.close()

    def write(self, data: dict):
        database = sqlite3.connect(self.db_name)
        csr = database.cursor()
#         row_data_string = ""
#         for _ in list(self.row_data):
#             row_data_string += f"{_} text, "

#         row_data_string = row_data_string.strip(", ")
#         create_table = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({row_data_string})"
        self.create_table_if_not_exists()
        qstion_marks = ""

        for _ in data:
            qstion_marks += "?, "

        qstion_marks = qstion_marks.strip(", ")
        insert_data = f"INSERT INTO {self.table_name} VALUES ({qstion_marks})"
        csr.execute(insert_data, tuple(data.values()))
        database.commit()
        database.close()

        return True

    def search(self):
        self.create_table_if_not_exists()
        database = sqlite3.connect(self.db_name)
        c = database.cursor()
        data = c.execute(f"SELECT * FROM {self.table_name}").fetchall()
        database.close()
        return data

    def update(self):
        pass

    def delete(self):
        pass
