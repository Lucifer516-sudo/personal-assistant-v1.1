"""
## Doc String ##
"""

from src.core.logger.log_statements import Logging # Logging() --> class
from rich import print as rprint

class Text():
    def __init__(self,text):
        self.text = text
        __type__ = "Text"

    def split_by_space(self):
        return str(self.text).split(" ")

    def split_by_comma(self):
        return str(self.text).split(",")
#
#    def pprint(self):
#        rprint(self.text)
#        return None

class Censored(Text):
    def __init__(self,text) -> None:
        self.text = text

    def censor(self):
        # Shall only be used while logging
        if self.__init__.__type__ == "Text" or self.__init__.__type__ == "Password" :
            pass
    
        
    def uncensor(self):
        # Raises error on censor()
        ...

class Password(Text):
    def __init__(self, text):
        super().__init__(text)

class Email(Text):
    def __init__(self, text):
        super().__init__(text)

class DOB(Text):
    def __init__(self, text):
        super().__init__(text)

c = Censored("test text")
print((c.censor))
#print(c.censor())
