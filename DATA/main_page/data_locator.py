from dataclasses import dataclass
from selenium.webdriver.common.by import By
from DATA.data_test import Locator


@dataclass
class TopNavigationBarLocators:
    menu: Locator = Locator(By.CLASS_NAME, 'header2021-portals')
    menu_elements: Locator = Locator(By.CLASS_NAME, 'header2021-portal')