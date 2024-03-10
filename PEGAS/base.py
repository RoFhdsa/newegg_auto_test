import os
import secrets
import string
from datetime import datetime
from telnetlib import EC

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Base:
    """Предоставляет методы для работы с веб-элементами."""

    def __init__(self, driver: WebDriver):
        """
        Инициализирует экземпляр класса Base.

        Args:
            driver (WebDriver): Экземпляр WebDriver для взаимодействия с браузером.
        """
        self.driver = driver

    def wait_for_element(self, by: By, locator: str, timeout=10):
        """
        Ожидает появления элемента на странице.

        Args:
            by (By): Метод поиска элемента (например, By.ID, By.CLASS_NAME).
            locator (str): Локатор элемента.
            timeout (int, optional): Максимальное время ожидания в секундах (по умолчанию 10).

        Returns:
            WebElement: Элемент, если найден.

        Raises:
            TimeoutException: Если элемент не был найден за указанное время.
            NoSuchElementException: Если элемент не был найден.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, locator)))
            return element
        except TimeoutException:
            raise TimeoutException(
                f"Элемент с локатором '{locator}' по средствам '{by}' не был найден за {timeout} секунд")
        except NoSuchElementException:
            raise NoSuchElementException(f"Элемент с локатором '{locator}' по средствам '{by}' не был определен")


    def click(self, by: By, locator: str, timeout=10):
        """
        Выполняет клик по элементу.

        Args:
            by (By): Метод поиска элемента (например, By.ID, By.CLASS_NAME).
            locator (str): Локатор элемента.
            timeout (int, optional): Максимальное время ожидания в секундах (по умолчанию 10).

        Raises:
            TimeoutException: Если элемент не был найден за указанное время.
            NoSuchElementException: Если элемент не был найден.
        """
        try:
            element = self.wait_for_element(by, locator, timeout)
            element.click()
        except TimeoutException:
            raise TimeoutException(
                f"Элемент с локатором '{locator}' по средствам '{by}' не был найден за {timeout} секунд")
        except NoSuchElementException:
            raise NoSuchElementException(f"Элемент с локатором '{locator}' по средствам '{by}' не был определен")


    def remove_element(self, by: By, locator: str, timeout=10):
        """
        Удаляет элемент на странице.

        Args:
            by (By): Метод поиска элемента (например, By.ID, By.CLASS_NAME).
            locator (str): Локатор элемента.
            timeout (int, optional): Максимальное время ожидания в секундах (по умолчанию 10).

        Raises:
            TimeoutException: Если элемент не был найден за указанное время.
            NoSuchElementException: Если элемент не был найден.
        """
        try:
            element = self.wait_for_element(by, locator, timeout)
            self.driver.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", element)
        except TimeoutException:
            raise TimeoutException(f"Элемент с локатором '{locator}' по средствам '{by}' не был найден за {timeout} секунд")
        except NoSuchElementException:
            raise NoSuchElementException(f"Элемент с локатором '{locator}' по средствам '{by}' не был определен")

    def find_element(self, by: By, locator: str):
        """
        Находит элемент на странице.

        Args:
            by (By): Метод поиска элемента (например, By.ID, By.CLASS_NAME).
            locator (str): Локатор элемента.

        Returns:
            WebElement: Найденный элемент.

        Raises:
            NoSuchElementException: Если элемент не был найден.
        """
        try:
            return self.driver.find_element(by, locator)
        except NoSuchElementException:
            raise NoSuchElementException(f"Элемент с локатором '{locator}' по средствам '{by}' не был найден")

    def find_elements(self, by: By, locator: str):
        """
        Находит все элементы на странице.

        Args:
            by (By): Метод поиска элемента (например, By.ID, By.CLASS_NAME).
            locator (str): Локатор элемента.

        Returns:
            List[WebElement]: Найденные элементы.

        Raises:
            NoSuchElementException: Если элементы не были найдены.
        """
        try:
            return self.driver.find_elements(by, locator)
        except NoSuchElementException:
            raise NoSuchElementException(f"Элементы с локатором '{locator}' по средствам '{by}' не были найдены")

    def scroll_into_view(self, element):
        """
        Прокручивает страницу так, чтобы элемент был виден.

        Args:
            element (WebElement): Элемент, который должен быть виден.
        """
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def return_actual_url(self):
        """
        Возвращает текущий URL страницы.

        Returns:
            str: Текущий URL страницы.
        """
        return self.driver.current_url

    def create_screenshot(self, name_screenshot: str) -> str:
        """
        Создает скриншот страницы.

        Args:
            name_screenshot (str): Имя скриншота.

        Returns:
            str: Путь к созданному скриншоту.
        """
        alph = string.digits + string.ascii_uppercase
        id = ''.join(secrets.choice(alph) for r in range(32))
        path = f'{self.create_dir()}{os.path.sep}{name_screenshot}{id}.png'
        self.driver.get_screenshot_as_file(path)
        return path

    @staticmethod
    def create_dir() -> str:
        """
        Создает директорию для сохранения логов и скриншотов.

        Returns:
            str: Путь к созданной директории.
        """
        path = f'logs_files{os.path.sep}{datetime.now().strftime("%Y-%m-%d")}'
        os.makedirs(path, exist_ok=True)
        return path
