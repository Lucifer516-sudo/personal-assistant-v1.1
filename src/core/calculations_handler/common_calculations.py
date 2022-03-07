from statistics import fmean
from typing import List
from ..logger.log_statements import Logging
from ..global_info import file_name


class Statistics():

    def __init__(self):
        self.logger = Logging(0)
        self.log = self.logger.log
        self.log(f"On >> class: Statistics :: Statistics.__init__ << {file_name(__file__)}")

    def avg(self, values: List[float]):
        self.log(f"On >> class: Statistics :: Statistics.avg << {file_name(__file__)}")
        return fmean(values)

    def percentile(self, x, total_x):
        self.log(f"On >> class: Statistics :: Statistics.percentile << {file_name(__file__)}")
        return (x/total_x) * 100


print(Statistics().avg(values=[1.0, 2.0]))
