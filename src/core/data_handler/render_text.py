"""
$$ IMPORTANT $$
    @ This module should only be used while logging passwdords


render_text.py
--------------
[*] this is the base class which will take care of most of the stuffs for rendering
    text


"""
from ..logger.log_statements import Logging   # Logging() --> class
from ..global_info import file_name
import traceback


class Text():
    def __init__(self, text):
        self.text = text
        self.__real_text__ = self.text
        self.__type__ = "TEXT"
        self.logger = Logging(0)
        self.log = self.logger.log
        self.log(f"On >> class: Text :: Text.__init__ << {file_name(__file__)}")

    def split_by_space(self):
        self.log(f"On >> class: Text :: Text.split_by_space << {file_name(__file__)}")
        return str(self.text).split(" ")

    def split_by_comma(self):
        self.log(f"On >> class: Text :: Text.split_by_comma << {file_name(__file__)}")
        return str(self.text).split(",")

    def censor(self):
        self.log(f"On >> class: Text :: Text.censor << {file_name(__file__)}")
        self.text = str("$_C3NS0R3D_$")
        return self.text

    def uncensor(self):
        self.log(f"On >> class: Text :: Text.uncensor << {file_name(__file__)}")
        return self.__real_text__

    def class_name_and_method(self):
        return __class__.__name__, traceback.extract_stack(None, 2)[0][-1][-3]


a = Text("Test")
print(a.censor())

print(a.uncensor())

print(a.class_name_and_method())
