import os
import pathlib
import datetime

FOLDER_NAME = "PAL"
DB_FOLDER_NAME = "PAL-DB"
ACCOUNTS_DB_NAME = "PAL-ACCOUNTS-DB"  # Folder

# Main DB :
MAIN_DB_NAME = "PAL_MAIN"  # File
MAIN_DB_TABLE_NAME = "ALL_ACCOUNTS_NAME"
MAIN_DB_ROW_ONE = [
        "ACCOUNT_NAME",
        "DATE_TIME_CREATED",
        "PATH_LOCATED",
        "PASSWORD_HASH"
        ]

# Logs DB
LOGS_DB_FOLDER = "PAL-LOGS"
LOGS_DB_NAME = "PAL_LOGS"
LOGS_DB_TABLE_NAME = "LOGS"
LOGS_DB_ROW_ONE = [
        "DATE_AND_TIME",
        "LOG_STATEMENT",
        "LOG_LEVEL"
        ]


# Account DB :
ACCOUNT_DB_TABLE_NAME = "ACCOUNT_DETAILS"
ACCOUNT_DB_ROW_ONE = [
        "USER_NAME",
        "USER_EMAIL",
        "USER_DOB",
        "USER_PASSWD"
        ]

# # Wolframalpha DB :
# WOLFRAMALPHA_QUERY_DB_NAME = "WOLFRAMALPHA_QUERY_DB"  # File
# WOLFRAMALPHA_QUERY_DB_TABLE_NAME = "WOLFRAMALPHA_QUERY_INFO"
# WOLFRAMALPHA_QUERY_DB_ROW = [
#         "QUERY_DATE",
#         "QUERY_TIME",
#         "QUERY",
#         "QUERY_RESULT"
#         ]
#

def HOME_DIR():
    return str(pathlib.Path.home())


def file_name(file):
    files_splitted = str(file).split("/")
    return files_splitted[-1]

def format_name(user_name: str):
    user_name = user_name.replace(" ","_")
    return  user_name +"__" + str(((str(datetime.datetime.now())).replace(":","~")).split(".")[0])



MAIN_DB_PATH = str(f"{HOME_DIR()}{os.path.sep}{FOLDER_NAME}{os.path.sep}{DB_FOLDER_NAME}{os.path.sep}{MAIN_DB_NAME}.db")

ACCOUNTS_DB_PATH = str(f"{HOME_DIR()}{os.path.sep}{FOLDER_NAME}{os.path.sep}{DB_FOLDER_NAME}{os.path.sep}{ACCOUNTS_DB_NAME}")

# WOLFRAMALPHA_QUERY_DB_PATH = str(f"{HOME_DIR()}{os.path.sep}{FOLDER_NAME}{os.path.sep}{DB_FOLDER_NAME}{os.path.sep}{WOLFRAMALPHA_QUERY_DB_TABLE_NAME}.db")

LOGS_DB_PATH = str(f"{HOME_DIR()}{os.path.sep}{FOLDER_NAME}{os.path.sep}{LOGS_DB_FOLDER}{os.path.sep}{LOGS_DB_NAME}.db")

# All Modules Being imported
ALL_MODULES_IMPORTED = [
        "os",
        "subprocess",
        "pathlib",
        "math",
        "rich"
        ]

# get the modules list
ALL_MODULES_IMPORTED.sort()

# def blr_plt_l_stmt(_class__, filename):
#     func_name = traceback.extract_stack(None, 2)[0][2]
#
#     blr_plate = f"On >> class: {_class__.__name__} :: {_class__.__name__}.{func_name()} << {file_name((filename))}"
#     return blr_plate
#
SLEEP_INTERVALS = [
    0.012720191586123919,
    0.7655287147407026,
    0.3994295586396437,
    0.2583703881046321,
    0.70977364243239,
    0.36000782454443014,
    0.7220175214467037,
    0.741862040102285,
    0.9451891773173736,
    0.35198548756881554,
    0.6987872829605946,
    0.7046381741762546,
    0.6178895274815066,
    0.7214604626985551,
    0.9010047641488468,
    0.4367800399695887,
    0.7955017150832352,
    0.9078909826249789,
    0.17981264710790157,
    0.9736775562132168,
    0.2539717360407776,
    0.5293673808151873,
    0.07098886388737535,
    0.8673392295173815,
    0.5162775528978254,
    0.12045470613888654,
    0.5030247039049968,
    0.49036229104318907,
    0.2361335508895389,
    0.2140383732669381,
    0.4110816973891287,
    0.8258499830759795,
    0.10963849031468809,
    0.39573433427382554,
    0.7034390315418311,
    0.9924848290689988,
    0.2777052984685714,
    0.2018651563929047,
    0.6527590063482696,
    0.8532395110551534,
    0.9446663520037634,
    0.07147395298706527,
    0.34021037312895386,
    0.26314530223889276,
    0.47035663181897647,
    0.6760381670891521,
    0.390544712507253,
    0.3144640908555709,
    0.7352501092832768,
    0.6899224941248204
]
