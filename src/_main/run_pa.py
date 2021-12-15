import os
os.system("clear") # This statement works on debian | linux based systems
print(f"Hello Sir :) \n Welcome Back to the Program ...")
print(f"Getting started .....")

from src._main.prechecks.check_for_main_dir_if_not_exists_create_it import preckeck_one
from src.core.load_screen_printer.load_screen import loading_screen_module_importer
from src._main.prechecks.function_check_internet import ping_internet
from rich.console import Console
from time import sleep

c = Console()

def up_or_down(rtn: bool):
    if rtn == True:
        return str("OK COOL !")
    else :
        return str("ERROR :(")

def start_up():
    db_available = True
    ac_db_available = True
    wolfram_db_available = True
    wiki_db_available = True
    internet_available = ping_internet()

    if not preckeck_one(): # This ain't the most apt way to do this tho
        db_available =  False
        ac_db_available = False
        wiki_db_available = False
        wolfram_db_available = False

    if internet_available != True:
        internet_available = False
    
    sleep(2)
    loading_screen_module_importer()
    sleep(2)
    c.clear()
    config_check_op = f"""
[i]Main DataBase Available         [/] - [b][magenta]{up_or_down(db_available)}[/][/]
[i]Accounts DataBase Available     [/] - [b][magenta]{up_or_down(ac_db_available)}[/][/]
[i]Wolframalpha DataBase Available [/] - [b][magenta]{up_or_down(wolfram_db_available)}[/][/]
[i]Wikipedia DataBase Available    [/] - [b][magenta]{up_or_down(wiki_db_available)}[/][/]
[i]Necessary Modules Available     [/] - [b][magenta]OK COOL ![/][/]
[i]Internet Available              [/] - [b][magenta]{up_or_down(internet_available)}[/][/]
    """
    c.print(config_check_op)


start_up()

# Show the main menu

