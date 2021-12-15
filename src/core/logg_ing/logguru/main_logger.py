from loguru import logger as lgr
import datetime
import os

info        = lgr.info
debug       = lgr.debug
warn        = lgr.warning
critical    = lgr.critical
catch = lgr.catch


@catch
def current_file_name(file_name: str):
    """
    current_file_name(file_name: str)
    --------------------------------------------------
    This function returns the current running file name
    using `__file__`
    :params:
    -->     file_name: str
    """
    try:
        info(f"Returing file name using {file_name}")
        return str(file_name.split("/")[-1])
    except:
        critical(f"There has been error !")
        raise Exception("Not a File")

@catch
def current_file_name_without_extension(file_name: str):
    """
    current_file_name_without_extension(file_name: str)
    --------------------------------------------------
    This function returns the current running file name
    using `__file__` and trims off the extension
    :params:
    -->     file_name: str
    """
    try:
        info(f"Returing file name w/o extension using {file_name}")
        file_name_with_ext =  str(file_name.split("/")[-1])
        debug(f"The File Name w/o extension is : {file_name_with_ext.split('.')[0]}") # The correct method would be to remove the last item in the list
        return file_name_with_ext.split(".")[0]
    except:
        critical(f"There has been error !")
        raise Exception("Not a File")

@catch
def add_log_folder(directory: str):
    """
    This function adds the `logs` folder in file folder
    """
    folders = os.listdir(directory)
    info("Checking if the logs folder is in the files directory")
    if 'logs' not in list(folders):
        os.mkdir(f"{directory}/logs")
        debug(f"Added the logs folder : {directory}/logs")

@catch
def add_log_file(file_name: str):
    """
    add_log_file(file_name=None)
    ---------------------------------------------------
    This function adds a new log file with the datetime
    :params:
    -->     file_name: None
    """
    cwd = os.getcwd()
    add_log_folder(cwd)
    cur_date_time = str(datetime.datetime.now()).replace(" ","_at_")
    cur_date_time = cur_date_time.replace(":","~")
    cur_date_time = cur_date_time.replace(".","_ms_")
    lgr.add(f"{cwd}/logs/{current_file_name_without_extension(file_name)}__{cur_date_time}.log",diagnose=True)
    file_name = f"{cwd}/logs/{current_file_name(file_name)}__{cur_date_time}.log"
    info(f"Added the Log File : {file_name}")



