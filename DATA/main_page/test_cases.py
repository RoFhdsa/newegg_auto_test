from DATA.data_test import TestFactory, PositiveTestCase, NegativeTestCase
from DATA.main_page.data_test_case import MainPageTestCase, MainPageResultCheck

# Создаем экземпляр фабрики
factory = TestFactory()

# Регистрируем классы тестовых случаев
factory.register_test_case("positive", PositiveTestCase)
factory.register_test_case("negative", NegativeTestCase)

positive_test_case = MainPageTestCase()
negative_test_case = MainPageTestCase(is_top_bar_menu=True, name_title_menu='any_text')

positive_result_check = MainPageResultCheck(result=True)
negative_result_check = MainPageResultCheck(result=None)

test_cases_collection = [
    factory.create_test_case("positive", positive_test_case, positive_result_check),
    factory.create_test_case("negative", negative_test_case, negative_result_check)
]
