"""
Тест на доступность главной страницы

Проверить наличия:

Проверить наличие основных элементов интерфейса: верхнее меню навигации

Проверить наличие основных элементов интерфейса: Dark Mode

Проверить наличие основных элементов интерфейса: корзина

Проверить наличие основных элементов интерфейса: СТРАНЫ И РЕГИОНЫ

Проверить наличие основных элементов интерфейса: поискового окна

Проверить наличие основных элементов интерфейса: рекламного баннера

Проверить наличие основных элементов интерфейса: борд-меню слева

Проверить наличие основных элементов интерфейса: Популярные продукты

Проверить наличие основных элементов интерфейса: борд-меню нижнее

Проверить наличие основных элементов интерфейса: ЛК
"""
import allure
import pytest

from DATA.main_page.test_cases import test_cases_collection


class TestMainPage:
    @allure.title("Тест проверки отображения страницы продуктов")
    @allure.description("Проверка отображения страницы продуктов для разных типов пользователей")
    @pytest.mark.parametrize("test_cases_collection", test_cases_collection)  # Используем параметризацию с заранее подготовленными тестовыми случаями
    def test_check_products(self, top_navigation_bar, test_cases_collection):
        expected_result_test = test_cases_collection.expected_result_test.result
        data_case = test_cases_collection.data_case
        with allure.step(f"Проверка верхнего меню"):
            result_test = top_navigation_bar.check_menu_element_by_title(title=data_case.name_title_menu)
            allure.attach(f"Ожидаемые результаты: {expected_result_test}", name="Expected Results",
                          attachment_type=allure.attachment_type.TEXT)
            allure.attach(f"Фактический результат: {result_test}", name="Actual Result",
                          attachment_type=allure.attachment_type.TEXT)
            assert expected_result_test == result_test

        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.link("https://tracker.yandex.ru/WAT-2", name="Задача:   WAT-2: Тест на доступность главной страницы")

