class Login:
    def __init__(self, user_name: str, user_passwd: bytes) -> None:
        self.user_name = user_name
        self.user_passwd = user_passwd

    def authorize(self):
        pass  # have to connect to db and search the data
