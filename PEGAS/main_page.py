from selenium.webdriver.remote.webelement import WebElement

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

    def get_menu_elements(self) -> list[WebElement]:
        """Получает все элементы верхнего меню навигации."""
        return self.wait_for_element(*self.menu_locator)

    def get_menu_element_by_title(self) -> WebElement:
        self.click_blunk()
        """Получает элемент меню по заголовку."""
        elements = self.find_elements(*self.menu_elements_locator)

        for element in elements:
            # if title.lower() in element.text.lower():
            print(f' element = {element}')
            return element

    def click_menu_element_by_title(self, title: str):
        """Выполняет клик по элементу меню по заголовку."""
        element = self.get_menu_element_by_title(title)
        if element:
            element.click()
