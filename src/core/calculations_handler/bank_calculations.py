from ..calculations_handler.common_calculations import Statistics
from ..logger.log_statements import Logging
from ..global_info import file_name


class BankManager():
    def __init__(self) -> None:
        self.stats = Statistics
        self.logger = Logging(0)
        self.log = self.logger.log
        self.log(f"On >> class: BankManager :: BankManager.__init__ << {file_name(__file__)}")

    def SimpleInterest(self, p: float, n: int, r: float):
        return (p*n*r)/100

    def CompoundInterest(self, p: float, n: int, r: float, t: int):
        return (p*((n+(r/100))/n)**(n*t))
