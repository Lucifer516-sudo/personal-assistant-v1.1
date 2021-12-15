from src.core.global_info import ALL_MODULES_IMPORTED

def loading_screen_module_importer(modules_list=ALL_MODULES_IMPORTED):
    """
    This function returns the value True or False
    and imports all modules at the startup
    """
    all_modules_imported = False
    if True:
        from rich.console import Console
        from rich.progress import track
        from time import sleep
        from src.core.global_info import SLEEP_INTERVALS
        from colorama import Fore,Style,init
        import random
        import importlib as importer
    
        init(autoreset=True)
        c = Console()
        red = Fore.RED + Style.BRIGHT
        reset_clr = Fore.RESET
        for module in track(range(len(modules_list)),description="[Progress]=>"):
            importer.__import__(modules_list[module])
            print(f"Loaded {red}[{modules_list[module]}]{reset_clr} ...")
            sleep(random.choice(SLEEP_INTERVALS))

        all_modules_imported = True
    
    return all_modules_imported

