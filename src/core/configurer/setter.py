import os
import sys
import pathlib
import platform

from loguru import logger as lgr
from rich.traceback import install

from src.core.global_info import (
    ACCOUNTS_DB_NAME,
    ACCOUNTS_DB_PATH,
    DB_FOLDER_NAME,
    FOLDER_NAME,
    HOME_DIR,
    MAIN_DB_NAME,
    LOGS_DB_NAME,
    LOGS_DB_FOLDER,
)

catch = lgr.catch


@catch
def platform_checker():
    return str(platform.system())


@catch
def home_dir():
    """
    Function return the home directory
    """
    return str(pathlib.Path.home())


@catch
def make_the_home_dir_to_save_the_db():
    configured = True
    main_directory_created = True
    database_folder_created = True
    accounts_database_created = True
    database_file_created = True
    wolframalpha_db_created = True

    if True:
        dir_name = FOLDER_NAME
        database_folder_name = DB_FOLDER_NAME
        database_file_name = MAIN_DB_NAME
        dirs_in_home_folder = os.listdir(HOME_DIR())
        if FOLDER_NAME not in dirs_in_home_folder:
            os.mkdir(f"{HOME_DIR()}{os.path.sep}{FOLDER_NAME}")
            main_directory_created = False

        dirs_inside_dir_name = os.listdir(f"{HOME_DIR()}{os.path.sep}{dir_name}")
        if database_folder_name not in dirs_inside_dir_name:
            os.mkdir(f"{HOME_DIR()}{os.path.sep}{dir_name}{os.path.sep}{database_folder_name}")
            database_folder_created = False

        files_inside_db_folder = os.listdir(f"{HOME_DIR()}{os.path.sep}{dir_name}{os.path.sep}{database_folder_name}")
        if database_file_name not in files_inside_db_folder:
            os.system(f"touch {HOME_DIR()}{os.path.sep}{dir_name}{os.path.sep}{database_folder_name}{os.path.sep}{database_file_name}.db")
            database_file_created = False

        if ACCOUNTS_DB_NAME not in files_inside_db_folder:
            os.mkdir(f"{ACCOUNTS_DB_PATH}")
            accounts_database_created = False

# if f"{WOLFRAMALPHA_QUERY_DB_NAME}.db" not in os.listdir(f"{HOME_DIR()}{os.path.sep}{FOLDER_NAME}{os.path.sep}{DB_FOLDER_NAME}"):
# os.system(f"touch {HOME_DIR()}{os.path.sep}{FOLDER_NAME}{os.path.sep}{DB_FOLDER_NAME}{os.path.sep}{WOLFRAMALPHA_QUERY_DB_NAME}.db")
# wolframalpha_db_created = False

        if LOGS_DB_FOLDER not in os.listdir(f"{HOME_DIR()}{os.path.sep}{FOLDER_NAME}"):
            os.mkdir(f"{HOME_DIR()}{os.path.sep}{FOLDER_NAME}{os.path.sep}{LOGS_DB_FOLDER}")

        if f"{LOGS_DB_NAME}.db" not in os.listdir(f"{HOME_DIR()}{os.path.sep}{FOLDER_NAME}{os.path.sep}{LOGS_DB_FOLDER}"):
            os.system(f"touch {HOME_DIR()}{os.path.sep}{FOLDER_NAME}{os.path.sep}{LOGS_DB_FOLDER}{os.path.sep}{LOGS_DB_NAME}.db")
        if main_directory_created and database_folder_created and database_file_created and wolframalpha_db_created and accounts_database_created:
            configured = True
        else:
            configured = False


        return configured

def copy_program_folder_to_specified_directory():
    pass


main_program_statement = """
#!/data/data/com.termux/files/usr/bin/python
# -*- coding: utf-8 -*-
"""

def make_it_as_a_executable_program():
    make_the_home_dir_to_save_the_db()
    if True:
        print("Made The Exe Dir...")
#        files_n_folders_ = "personal-assistant-v1.1" in os.listdir(os.getcwd()+"/")
#        site_packs = str(os.getcwd()).find("/")
#        print(f"files_n_folders_: {files_n_folders_}\nsite_packs: {site_packs}\ncwd: {os.getcwd()}")
#        print(site_packs)
        if True:
            os.system(f"cp -r {os.getcwd()}/project/personal-assistant-v1.1/src {sys.exec_prefix}/lib/python3.10/site-packages/pal/")
            os.system(f"touch {sys.exec_prefix}/bin/pal")
            with open(f"{sys.exec_prefix}/bin/pal","w+") as f:
                f.write(main_program_statement)
                print(f"wrote\n{main_program_statement}\n...")

def main_setter():
    make_the_home_dir_to_save_the_db()
    make_it_as_a_executable_program()
    return True
