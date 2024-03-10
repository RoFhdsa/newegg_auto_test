from dataclasses import dataclass

from DATA.data_test import TestCaseData, ResultCheck


@dataclass
class MainPageTestCase (TestCaseData):
    is_top_bar_menu: bool = True

class MainPageResultCheck(ResultCheck):
    def __init__(self, result):
        self.result = result
        pass