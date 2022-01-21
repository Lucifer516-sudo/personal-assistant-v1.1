"""
## Doc String ##
"""

from src.core.logger.log_statements import Logging # Logging() --> class

class Text():
    def __init__(self,text):
        self.text = text

class Password(Text):
    def __init__(self, text):
        super().__init__(text)

class Email(Text):
    def __init__(self, text):
        super().__init__(text)

class DOB(Text):
    def __init__(self, text):
        super().__init__(text)
