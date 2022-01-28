import hashlib
from src.core.logger.log_statements import Logging
from src.core.global_info import file_name


class Hash:
    def __init__(self, text) -> None:
        self.text = text
        self.__length_of_text__ = len(str(self.text))
        self.logger = Logging(cout=1)
        self.log = self.logger.log

    def hash(self):
        self.log(log_statement=f"On >> method :: Hash.hash << {file_name(__file__)}")
        return hashlib.sha512(self.text).hexdigest().encode()
