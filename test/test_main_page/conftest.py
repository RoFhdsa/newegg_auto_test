import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from DATA.data_connect import URL
from PEGAS.main_page import MainPage, TopNavigationBar


@pytest.fixture()
def drivers():
    """инициализация драйвера"""

    # Создаем экземпляр драйвера Chrome
    driver = webdriver.Chrome()

    # Открываем страницу с CAPTCHA
    driver.get(URL().url)

    try:
        # Ждем, пока кнопка "I'm not a robot" станет кликабельной
        checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="checkbox"]')))

        # Нажимаем на кнопку "I'm not a robot"
        checkbox.click()

        # Далее вы можете выполнить другие необходимые действия для прохождения CAPTCHA

        # Переходим на главную страницу
        driver.get(URL().url)

        yield driver

    finally:
        # Важно закрыть браузер после выполнения теста
        driver.quit()


@pytest.fixture
def main_page(drivers):
    """Предоставляет объект для работы с главной страницей."""
    return MainPage(drivers)


@pytest.fixture
def top_navigation_bar(drivers):
    """Предоставляет объект для работы с главной страницей."""
    return TopNavigationBar(drivers)
