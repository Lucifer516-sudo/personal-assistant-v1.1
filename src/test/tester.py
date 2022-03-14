from time import perf_counter, sleep
###################################
# Application Imports
from src.core.configurer import setter
from src.core.accounts_handler.main_accounts_handler import Account
###################################

configuration_result = False
ac_create_result = False

def Setter():
    import os
    import pathlib
    import sys
    print("Imported os and pathlib ...")
    if "PAL" in os.listdir(pathlib.Path.home()):
        os.system("rm -rf ~/PAL")
        print("Removed ~/PAl directory ...")
        if "pal" in os.listdir(sys.prefix+"/bin"):
            print(f"Prev Instance of `pal` in {sys/prefix}/bin")
            os.system(f"rm -rf {sys.prefix}/bin/pal")
            print("removed previous instance of pal")


    if True:
        print("Trying to create one ... ")
        setter.main_setter()
        configuration_result = True

    return configuration_result

def Create_ACs():
    if True:
        test_user_names = ["User 1", "User 2", "User 3"]
        test_user_email  = ["Email 1", "Email 2", "Email 3"]
        test_user_dob    = ["dd1-mm1-yyyy1", "dd2-mm2-yyyy2", "dd3-mm3-yyyy3"]
        test_user_passwd = ["passwd1", "passwd2", "passwd3"]
        for i in range(3):
            ac = Account(test_user_names[i], test_user_email[i], test_user_dob[i], test_user_passwd[i])
            if ac.create_account():
                ac_create_result = True
            else:
                ac_create_result = False
def main():
    Setter()
    Create_ACs()

if __name__ == "__main__":
    main()
