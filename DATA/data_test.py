from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class Locator:
    by: By
    value: str


@dataclass
class TestCaseData:
    pass


class ResultCheck:

    def __init__(self, ):
        pass

    def __eq__(self, other):
        return all(getattr(self, attr) == getattr(other, attr) for attr in self.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __del__(self):
        pass


class TestCase:
    def __init__(self, data_case, expected_result_test):
        self.expected_result_test = expected_result_test
        self.data_case = data_case

    def return_case(self):
        return {
            "data_case": self.data_case,
            "result_test": self.expected_result_test
        }

class TestFactory:
    def __init__(self):
        self.test_case_classes = {}

    def register_test_case(self, type_case, test_case_class):
        self.test_case_classes[type_case] = test_case_class

    def create_test_case(self, type_case, data_case, expected_result_test):
        if type_case not in self.test_case_classes:
            raise ValueError(f"Unknown type_case: {type_case}")
        return self.test_case_classes[type_case](data_case, expected_result_test)

class PositiveTestCase(TestCase):
    def __init__(self, data_case, expected_result_test):
        super().__init__(data_case, expected_result_test)
    pass
class NegativeTestCase(TestCase):
    def __init__(self, data_case, expected_result_test):
        super().__init__(data_case, expected_result_test)
    pass

