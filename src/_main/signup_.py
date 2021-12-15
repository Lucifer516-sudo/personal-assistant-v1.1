from src.core.PA_ACs._ACs import Account
from getpass import getpass, getuser

def ask_the_user(user_name,user_email,user_dob,user_passwd):
    USER = Account(user_name=user_name,user_email=user_email,user_dob=user_dob,user_passwd=user_passwd)
    USER._create_account()

if __name__ == "__main__":
    name = getuser()
    dob = str(input("Enter ur DOB : "))
    email = str(input("Enter ur Email"))
    passwd = getpass("Enter Password or PassPhrase : ")

    ask_the_user(name,email,dob,passwd)
