from selenium.webdriver.remote.webelement import WebElement
import re
from DATA.main_page.data_locator import TopNavigationBarLocators
from PEGAS.mediator import Mediator


class MainPage(Mediator):
    def __init__(self, driver):
        super().__init__(driver)



    pass


class TopNavigationBar(MainPage):
    """Класс для работы с верхним меню навигации на сайте."""

    def __init__(self, driver):
        super().__init__(driver)
        self.menu_locator = TopNavigationBarLocators().menu
        self.menu_elements_locator = TopNavigationBarLocators().menu_elements

    def check_menu_element_by_title(self, title) -> WebElement:
        self.click_blunk()
        """Получает элемент меню по заголовку."""
        elements = self.find_elements(self.menu_elements_locator.by, self.menu_elements_locator.value)

        for element in elements:
            web_element_attributes = WebElementAttributes(element)
            web_title = web_element_attributes.attributes.get("title")
            # print(f' title = {web_element_attributes}')
            if web_title in title:
                return True

class WebElementAttributes:
    def __init__(self, web_element):
        """
        Инициализирует объект WebElementAttributes.

        Args:
            web_element: Объект WebElement, из которого извлекаются атрибуты.
        """
        self.attributes = {}  # Словарь для хранения атрибутов в формате {имя_атрибута: значение_атрибута}

        # Получаем внешний HTML-код элемента и находим все атрибуты с их значениями
        outer_html = web_element.get_attribute("outerHTML")
        matches = re.findall(r'(\w+)\s*=\s*"(.*?)"', outer_html)

        # Заполняем словарь атрибутами и их значениями
        for key, value in matches:
            self.attributes[key] = value.strip()

    def __str__(self):
        """
        Возвращает строковое представление объекта WebElementAttributes.

        Returns:
            str: Строковое представление объекта с атрибутами и их значениями.
        """
        # Преобразуем словарь атрибутов в строку с разделителем "\n" и возвращаем
        return "\n".join([f"{key}=\"{value}\"" for key, value in self.attributes.items()])

