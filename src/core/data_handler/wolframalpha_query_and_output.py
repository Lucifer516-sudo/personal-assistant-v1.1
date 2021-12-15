from loguru import logger as lgr

from src.core.configurer.directories_creator import make_the_home_dir_to_save_the_db
from src.core.global_info import (
    WOLFRAMALPHA_QUERY_DB_PATH,
    WOLFRAMALPHA_QUERY_DB_ROW,
    WOLFRAMALPHA_QUERY_DB_TABLE_NAME,
)
catch = lgr.catch

def add_wolframalpha_query_and_output_to_the_database(query_date: str, query_time: str, query: str, query_result: str):
    query_result_added = False
    try:
        make_the_home_dir_to_save_the_db()
        import sqlite3
        db = sqlite3.connect(WOLFRAMALPHA_QUERY_DB_PATH)
        c = db.cursor()
        create_table_in_the_db = f"create table if not exists {WOLFRAMALPHA_QUERY_DB_TABLE_NAME} ( {WOLFRAMALPHA_QUERY_DB_ROW[0]} text, {WOLFRAMALPHA_QUERY_DB_ROW[1]} text, {WOLFRAMALPHA_QUERY_DB_ROW[2]} text, {WOLFRAMALPHA_QUERY_DB_ROW[3]} text "
        add_wolframalpha_query_and_output_to_the_table = f"insert into {WOLFRAMALPHA_QUERY_DB_TABLE_NAME} values (?, ?, ?, ?)"
        c.execute(create_table_in_the_db)
        c.execute(add_wolframalpha_query_and_output_to_the_table,(query_date, query_time,query, query_result))
        db.commit()
        db.close()
        query_result_added = True
    except:
        print([WOLFRAMALPHA_QUERY_DB_TABLE_NAME,WOLFRAMALPHA_QUERY_DB_PATH,WOLFRAMALPHA_QUERY_DB_ROW])
        query_result_added = False

    return query_result_added


print(add_wolframalpha_query_and_output_to_the_database(query_date="date",query_time="time",query="query",query_result="result"))
