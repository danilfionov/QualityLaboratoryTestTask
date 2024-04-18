import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class Base_Page:
    """
    Инициализация страницы
    """
    def __init__(self, driver):
        self.url = None
        self.driver = driver

    """
    Открытие url
    """

    def open(self):
        self.driver.get(self.url)

    def page_loaded(self, timeout=10):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    """ 
    Проверка на видимость элемента 
    """

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();", element)

    def text_is_present_in_element(self, locator, expected_text, timeout=5):
        return Wait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, expected_text))

    def text_is_present_in_element_value(self, locator, expected_text, timeout=5):
        return Wait(self.driver, timeout).until(EC.text_to_be_present_in_element_value(locator, expected_text))

    """ 
    Поиск первого нужного элемента, 3 цикла
    """

    def get_first_element(self, collection, element_name):
        tries = 1
        while tries <= 3:
            for value in collection:
                locator = By.XPATH, value.format(element_name)
                elements = self.driver.find_elements(*locator)
                visible_elements = [element for element in elements if element.is_displayed()]
                if visible_elements:
                    if self.element_is_visible(locator):
                        return locator
            time.sleep(tries)
            tries += 1

    def get_first_element_in_window(self, window, collection, element_name):
        tries = 1
        while tries <= 3:
            for value in collection:
                value = window[1] + value
                locator = By.XPATH, value.format(element_name)
                elements = self.driver.find_elements(*locator)
                visible_elements = [element for element in elements if element.is_displayed()]
                if visible_elements:
                    if self.element_is_visible(locator):
                        return locator
            time.sleep(tries)
            tries += 1

    def get_all_elements(self, collection, element_name):
        tries = 1
        while tries <= 3:
            for value in collection:
                locator = By.XPATH, value.format(element_name)
                elements = self.driver.find_elements(*locator)
                visible_elements = [element for element in elements if element.is_displayed()]
                if visible_elements:
                    return visible_elements
            time.sleep(tries)
            tries += 1
