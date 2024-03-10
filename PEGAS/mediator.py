import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from PEGAS.base import Base


import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from PEGAS.base import Base

class Mediator(Base):
    """Содержит методы для работы с элементами, специфичными для вашего веб-приложения."""

    def __init__(self, driver):
        super().__init__(driver)

    def check_element(self, by: By, locator: str, timeout=10):
        """
        Проверяет наличие элемента на странице.

        Args:
            by (By): Метод поиска элемента (например, By.ID, By.CLASS_NAME).
            locator (str): Локатор элемента.
            timeout (int, optional): Максимальное время ожидания в секундах (по умолчанию 10).

        Returns:
            bool: True, если элемент найден, False в противном случае.
        """
        try:
            self.wait_for_element(by, locator, timeout)
            return True
        except TimeoutException:
            return False

    def select_box(self, by: By, locator: str, timeout=10):
        """
        Выбирает элемент.

        Args:
            by (By): Метод поиска элемента (например, By.ID, By.CLASS_NAME).
            locator (str): Локатор элемента.
            timeout (int, optional): Максимальное время ожидания в секундах (по умолчанию 10).

        Returns:
            bool: True, если элемент был успешно выбран, False в противном случае.
        """
        try:
            self.click(by, locator, timeout)
            return True
        except TimeoutException:
            return False

    def delete_element(self, by: By, locator: str, timeout=10):
        """
        Удаляет элемент со страницы.

        Args:
            by (By): Метод поиска элемента (например, By.ID, By.CLASS_NAME).
            locator (str): Локатор элемента.
            timeout (int, optional): Максимальное время ожидания в секундах (по умолчанию 10).

        Returns:
            bool: True, если элемент был успешно удален, False в противном случае.
        """
        try:
            element = self.wait_for_element(by, locator, timeout)
            self.driver.execute_script("arguments[0].remove();", element)
            return True
        except TimeoutException:
            return False

    def send_information(self, by: By, locator: str, data: str, timeout=10):
        """
        Вводит данные в поле.

        Args:
            by (By): Метод поиска элемента (например, By.ID, By.CLASS_NAME).
            locator (str): Локатор элемента.
            data (str): Данные, которые нужно ввести в поле.
            timeout (int, optional): Максимальное время ожидания в секундах (по умолчанию 10).

        Returns:
            bool: True, если данные были успешно введены в поле, False в противном случае.
        """
        try:
            element = self.wait_for_element(by, locator)
            element.send_keys(data)
            time.sleep(2)
            return True
        except TimeoutException:
            return False

    def click_blunk (self) -> None:
        action = ActionChains(self.driver)
        action.move_by_offset(0, 0).click().perform()