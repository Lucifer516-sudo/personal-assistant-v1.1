"""
$$ IMPORTANT $$
    @ This module should only be used while logging passwdords


render_text.py
--------------
[*] this is the base class which will take care of most of the stuffs for rendering
    text


"""
from src.core.logger.log_statements import Logging   # Logging() --> class
from src.core.global_info import file_name


class Text():
    def __init__(self, text):
        self.text = text
        self.__real_text__ = self.text
        self.__type__ = "TEXT"
        self.logger = Logging()
        self.log = self.logger.log
        self.log(f"On >> class: Text :: Text.__init__ << {file_name(__file__)}", cout=1)

    def split_by_space(self):
        self.log(f"On >> class: Text :: Text.split_by_space << {file_name(__file__)}", cout=1)
        return str(self.text).split(" ")

    def split_by_comma(self):
        self.log(f"On >> class: Text :: Text.split_by_comma << {file_name(__file__)}", cout=1)
        return str(self.text).split(",")

    def censor(self):
        self.log(f"On >> class: Text :: Text.censor << {file_name(__file__)}", cout=1)
        self.text = str("$_C3NS0R3D_$")
        return self.text

    def uncensor(self):
        self.log(f"On >> class: Text :: Text.uncensor << {file_name(__file__)}", cout=1)
        return self.__real_text__


a = Text("Test")
print(a.censor())

print(a.uncensor())
