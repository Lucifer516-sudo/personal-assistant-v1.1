class Logging:
    """
    Created this class just bcoz i currently dont know how to log the log info to a file tho
    """
    def __init__(self,date_time,log_statement) -> None:
        self.date_time = date_time # Date And Time to store to the database
        self.log_statement = log_statement # ANd log statement to log

    def log(self,cout=False):
        if cout != True:
            pass
        if cout == True:
            pass

