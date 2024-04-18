import calendar
import locale
import random
import string
import time
import re

import datetime

import pyautogui
from selenium.webdriver.support import expected_conditions as EC

import allure
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from QualityLaboratoryTestTask.python.ui.locators.Abstruct_Locators import Locators
from QualityLaboratoryTestTask.python.ui.pages.Base_Page import Base_Page


class Main_Page(Base_Page):
    """
    Проверка атрибута
    """

    @allure.step("Проверить, что у элемента {element_name} атрибут {attribute_name} равен {expected_value}.")
    def check_attribute_by_text_element(self, element_name, attribute_name, expected_value):
        element = self.get_first_element(Locators.Text.text, element_name)
        parent_element = self.driver.find_element(By.XPATH, element[1] + "/parent::*")
        actual_value = parent_element.get_attribute(attribute_name)
        assert actual_value == expected_value, \
            (f"Атрибут \"{attribute_name}\" у элемента \"{element_name}\" "
             f"не равен ожидаемому значению \"{expected_value}\".")
        (allure.attach(f"Атрибут \"{attribute_name}\" у элемента \"{element_name}\" "
                       f"равен ожидаемому значению \"{expected_value}\".",
                       attachment_type=allure.attachment_type.TEXT))

    @allure.step("Проверить, что у элемента {link_name} атрибут {attribute_name} равен {expected_value}.")
    def check_attribute_by_link_element(self, link_name, attribute_name, expected_value):
        element = self.get_first_element(Locators.Link.link, link_name)
        if link_name == 'Отмененные':
            actual_value1 = self.driver.find_element(By.XPATH, element[1] + "/parent::*/parent::*").get_attribute(
                attribute_name)
            actual_value2 = self.driver.find_element(By.XPATH, element[1] + "/parent::*").get_attribute(
                attribute_name)
            assert actual_value1 or actual_value2 == expected_value, \
                (f"Атрибут \"{attribute_name}\" у элемента \"{link_name}\" "
                 f"не равен ожидаемому значению \"{expected_value}\".")
            (allure.attach(f"Атрибут \"{attribute_name}\" у элемента \"{link_name}\" "
                           f"равен ожидаемому значению \"{expected_value}\".",
                           attachment_type=allure.attachment_type.TEXT))
        elif link_name == 'Внимание':
            actual_value = self.driver.find_element(By.XPATH, element[1] + "/parent::*/parent::*").get_attribute(
                attribute_name)
            assert actual_value == expected_value, \
                (f"Атрибут \"{attribute_name}\" у элемента \"{link_name}\" "
                 f"не равен ожидаемому значению \"{expected_value}\".")
            (allure.attach(f"Атрибут \"{attribute_name}\" у элемента \"{link_name}\" "
                           f"равен ожидаемому значению \"{expected_value}\".",
                           attachment_type=allure.attachment_type.TEXT))
        else:
            actual_value = self.driver.find_element(By.XPATH, element[1] + "/parent::*").get_attribute(attribute_name)
            assert actual_value == expected_value, \
                (f"Атрибут \"{attribute_name}\" у элемента \"{link_name}\" "
                 f"не равен ожидаемому значению \"{expected_value}\".")
            (allure.attach(f"Атрибут \"{attribute_name}\" у элемента \"{link_name}\" "
                           f"равен ожидаемому значению \"{expected_value}\".",
                           attachment_type=allure.attachment_type.TEXT))

    @allure.step("Проверить, что у чек-бокса {check_box_name} атрибут {attribute_name} {condition}.")
    def check_attribute_by_check_box_element(self, check_box_name, attribute_name, condition):
        element = self.get_first_element(Locators.Check_Box.check_box, check_box_name)
        child_element = ''
        try:
            child_element = self.driver.find_element(By.XPATH, element[1] + "/child::*").get_attribute(attribute_name)
        except NoSuchElementException:
            print("NoSuchElementException")
        if child_element:
            if condition == 'присутствует':
                assert child_element == 'true', \
                    (f"Атрибут \"{attribute_name}\" у элемента \"{check_box_name}\" "
                     f"не \"{condition}\".")
                (allure.attach(f"Атрибут \"{attribute_name}\" у элемента \"{check_box_name}\" \"{condition}\".",
                               attachment_type=allure.attachment_type.TEXT))
        else:
            element = self.driver.find_element(By.XPATH, element[1]).get_attribute(attribute_name)
            if condition == 'присутствует':
                assert element == 'true', \
                    (f"Атрибут \"{attribute_name}\" у элемента \"{check_box_name}\" "
                     f"не \"{condition}\".")
                (allure.attach(f"Атрибут \"{attribute_name}\" у элемента \"{check_box_name}\" \"{condition}\".",
                               attachment_type=allure.attachment_type.TEXT))

    """
    Шаги с полями
    """

    @allure.step("Заполнить поле {field_name} значением {text}.")
    def fill_field(self, field_name, text):
        if field_name == 'ТОВАР':
            element = By.XPATH, Locators.Fields.product_field
            assert self.element_is_visible(element), f"Поле \'{field_name}\' отсутствует."
            self.element_is_visible(element).clear()
            self.element_is_visible(element).send_keys(text)
        else:
            element = self.get_first_element(Locators.Fields.fields, field_name)
            assert self.element_is_visible(element), f"Поле \'{field_name}\' отсутствует."
            self.element_is_visible(element).clear()
            self.element_is_visible(element).send_keys(text)
        allure.attach(f"Поле \'{field_name}\' заполнено значением \'{text}\'.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Заполнить поле {field_name} под номером {field_number} значением {text}.")
    def fill_field_by_number(self, field_name, text, field_number):
        element = self.get_all_elements(Locators.Fields.fields, field_name)
        element = element[field_number - 1]
        assert element is not None, f"Поле \'{field_name}\' отсутствует."
        element.clear()
        element.send_keys(text)
        allure.attach(f"Поле \'{field_name}\' заполнено значением \'{text}\'.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Очистить поле {field_name}.")
    def clear_field(self, field_name):
        element = self.get_first_element(Locators.Fields.fields, field_name)
        assert self.element_is_visible(element), f"Поле \'{field_name}\' отсутствует."
        self.element_is_visible(element).clear()
        allure.attach(f"Поле \'{field_name}\' очищено.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Заполнить поле {field_name} значением {text}.")
    def fill_field_point(self, field_name, text, point):
        element = self.get_all_elements(Locators.Fields.fields_point, field_name)
        element = element[point]
        assert element, f"Поле \'{field_name}\' отсутствует."
        element.clear()
        element.send_keys(text)
        if field_name == 'Улица или место':
            try:
                ul = (By.XPATH, "//ul[@id='ui-id-2']")
                self.element_is_visible(ul)
                allure.attach(f"Поле \'{field_name}\' заполнено значением \'{text}\'.",
                              attachment_type=allure.attachment_type.TEXT)
            except TimeoutException:
                element.send_keys(" ")
                allure.attach(f"Поле \'{field_name}\' заполнено значением \'{text}\'.",
                              attachment_type=allure.attachment_type.TEXT)

    @allure.step("Проверить, что поле {field_name} заполнено значением {expected_text}.")
    def check_field_is_filled_value(self, field_name, expected_text):
        element = self.get_first_element(Locators.Fields.fields, field_name)
        assert self.element_is_visible(element), f"Поле \'{field_name}\' отсутствует."
        actual_text = self.element_is_visible(element).text
        if actual_text == '':
            actual_text = self.text_is_present_in_element_value(element, expected_text)
        else:
            actual_text = self.text_is_present_in_element(element, expected_text)
        assert actual_text is True, f"Значение \'{expected_text}\' отсутствует."
        allure.attach(f"Поле \'{field_name}\' заполнено значением \'{expected_text}\'.",
                      attachment_type=allure.attachment_type.TEXT)

    # get_field_value
    @allure.step("Получить текст у элемента {field_name}.")
    def get_field_value(self, field_name):
        if field_name == "Response":
            element = (By.XPATH, "//pre[@data-key='output-response']")
            assert self.element_is_visible(element), f"Поле \'{field_name}\' отсутствует."
            actual_text = self.element_is_visible(element).text
            return actual_text

    @allure.step("Проверить, что поле {field_name} заполнено значением {expected_text}.")
    def check_field_by_point(self, field_name, expected_text, point):
        element = self.get_all_elements(Locators.Fields.fields_point, field_name)
        element = element[point - 1]
        assert element, f"Поле \'{field_name}\' отсутствует."
        actual_text = element.get_attribute("value")
        assert actual_text == expected_text
        allure.attach(f"Поле \'{field_name}\' заполнено значением \'{expected_text}\'.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Очистить поле {field_name}.")
    def clear_field_point(self, field_name, point):
        element = self.get_all_elements(Locators.Fields.fields_point, field_name)
        element = element[point]
        assert element, f"Поле \'{field_name}\' отсутствует."
        element.clear()
        allure.attach(f"Поле \'{field_name}\' очищено.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Проверить, что поле {field_name} присутствует.")
    def check_field_exists(self, field_name):
        element = self.get_first_element(Locators.Fields.fields, field_name)
        assert self.element_is_visible(element), f"Поле \'{field_name}\' отсутствует."
        allure.attach(f"Поле \'{field_name}\' присутствует.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Проверить, что поле {field_name} отсутствует.")
    def check_field_not_exists(self, field_name):
        element = self.get_first_element(Locators.Fields.fields, field_name)
        assert element is None, f"Поле \'{field_name}\' присутствует."
        allure.attach(f"Поле \'{field_name}\' отсутствует.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Проверить, что поле {field_name} под номером {point} отсутствует.")
    def check_field_not_exists_by_point(self, field_name, point):
        element = self.get_all_elements(Locators.Fields.fields_point, field_name)
        try:
            element = element[point - 1]
        except IndexError:
            allure.attach(f"Поле \'{field_name}\' отсутствует.",
                          attachment_type=allure.attachment_type.TEXT)
            return
        raise SystemExit(f"Поле {field_name} присутствует")

    """
    Шаги с кнопками
    """

    @allure.step("Нажать на кнопку {button_name}.")
    def click_button(self, button_name):
        if button_name == "Закрыть":
            if self.page_loaded():
                element = self.driver.find_element(By.XPATH, Locators.Button.button_close)
                assert element, f"Кнопка \'{button_name}\' не найдена."
                self.element_is_clickable(element).click()
                allure.attach(f"Нажатие на кнопку \'{button_name}\'.",
                              attachment_type=allure.attachment_type.TEXT)
        elif button_name == "Редактировать":
            if self.page_loaded():
                element = self.driver.find_element(By.XPATH, Locators.Button.button_edit)
                assert self.element_is_visible(element), f"Кнопка \'{button_name}\' не найдена."
                self.element_is_clickable(element).click()
                allure.attach(f"Нажатие на кнопку \'{button_name}\'.",
                              attachment_type=allure.attachment_type.TEXT)
        elif button_name == "Плюс":
            if self.page_loaded():
                xpath = (By.XPATH, Locators.Button.button_plus)
                element = self.element_is_visible(xpath)
                assert element is not None, f"Кнопка \'{button_name}\' не найдена."
                self.element_is_clickable(element).click()
                allure.attach(f"Нажатие на кнопку \'{button_name}\'.",
                              attachment_type=allure.attachment_type.TEXT)
        elif button_name == "Отправить":
            if self.page_loaded():
                xpath = (By.XPATH, Locators.Button.button_send)
                element = self.element_is_visible(xpath)
                assert element is not None, f"Кнопка \'{button_name}\' не найдена."
                self.element_is_clickable(element).click()
                allure.attach(f"Нажатие на кнопку \'{button_name}\'.",
                              attachment_type=allure.attachment_type.TEXT)
        elif button_name == "Сохранить":
            if self.page_loaded():
                time.sleep(5)
                xpath = (By.XPATH, "//input[@type='submit' and @value='Сохранить']")
                element = self.element_is_visible(xpath)
                assert element is not None, f"Кнопка \'{button_name}\' не найдена."
                WebDriverWait(self.driver, 5).until(
                    EC.text_to_be_present_in_element_attribute((By.XPATH, xpath[1]), "class", "js-save-order"))
                element.click()
                WebDriverWait(self.driver, 5).until(
                    EC.text_to_be_present_in_element_attribute((By.XPATH, xpath[1]), "class", "js-save-order"))
                time.sleep(5)
                allure.attach(f"Нажатие на кнопку \'{button_name}\'.",
                              attachment_type=allure.attachment_type.TEXT)
        else:
            if self.page_loaded():
                element = self.get_first_element(Locators.Button.buttons, button_name)
                assert self.element_is_visible(element), f"Кнопка \'{button_name}\' не найдена."
                time.sleep(5)
                self.element_is_visible(element).click()
                allure.attach(f"Нажатие на кнопку \'{button_name}\'.",
                              attachment_type=allure.attachment_type.TEXT)

    @allure.step("Нажать на кнопку {button_name} под номером {button_number}.")
    def click_button_by_number(self, button_name, button_number):
        if button_name == "Закрыть":
            if self.page_loaded():
                element = self.elements_are_visible(By.XPATH, Locators.Button.button_close)
                element = element[button_number - 1]
                assert element is not None, f"Кнопка \'{button_name}\' не найдена."
                self.element_is_clickable(element).click()
                allure.attach(f"Нажатие на кнопку \'{button_name}\'.",
                              attachment_type=allure.attachment_type.TEXT)
        elif button_name == "Редактировать":
            if self.page_loaded():
                element = By.XPATH, Locators.Button.button_edit
                element = self.elements_are_visible(element)
                element = element[button_number - 1]
                assert element is not None, f"Кнопка \'{button_name}\' не найдена."
                self.element_is_clickable(element).click()
                allure.attach(f"Нажатие на кнопку \'{button_name}\'.",
                              attachment_type=allure.attachment_type.TEXT)
        elif button_name == "Плюс":
            if self.page_loaded():
                element = self.driver.find_elements(By.XPATH, Locators.Button.button_plus)
                element = element[button_number - 1]
                assert element is not None, f"Кнопка \'{button_name}\' не найдена."
                self.element_is_clickable(element).click()
                allure.attach(f"Нажатие на кнопку \'{button_name}\'.",
                              attachment_type=allure.attachment_type.TEXT)
        elif button_name == "История":
            if self.page_loaded():
                time.sleep(2)
                element = self.driver.find_elements(By.XPATH, Locators.Button.button_orders_history)
                element = element[button_number - 1]
                assert element is not None, f"Кнопка \'{button_name}\' не найдена."
                self.element_is_clickable(element).click()
                allure.attach(f"Нажатие на кнопку \'{button_name}\'.",
                              attachment_type=allure.attachment_type.TEXT)
        elif button_name == "Действие с адресом":
            if self.page_loaded():
                time.sleep(2)
                element = self.driver.find_elements(By.XPATH, Locators.Button.button_action_with_address)
                element = element[button_number - 1]
                assert element is not None, f"Кнопка \'{button_name}\' не найдена."
                self.element_is_clickable(element).click()
                allure.attach(f"Нажатие на кнопку \'{button_name}\'.",
                              attachment_type=allure.attachment_type.TEXT)
        elif button_name == "Удалить":
            if self.page_loaded():
                element = self.get_all_elements(Locators.Button_Type_Link.button_type_link, button_name)
                element = element[button_number - 1]
                assert element is not None, f"Кнопка \'{button_name}\' не найдена."
                self.element_is_clickable(element).click()
                allure.attach(f"Нажатие на кнопку \'{button_name}\'.",
                              attachment_type=allure.attachment_type.TEXT)
        else:
            if self.page_loaded():
                element = self.get_all_elements(Locators.Button.buttons, button_name)
                element = element[button_number - 1]
                assert element is not None, f"Кнопка \'{button_name}\' не найдена."
                time.sleep(2)
                self.element_is_clickable(element).click()
                allure.attach(f"Нажатие на кнопку \'{button_name}\'.",
                              attachment_type=allure.attachment_type.TEXT)

    @allure.step("Нажать на кнопку {button_name}, если она присутствует.")
    def if_button_exists_press(self, button_name):
        if button_name == "Закрыть":
            if self.page_loaded():
                try:
                    element = self.driver.find_element(By.XPATH, Locators.Button.button_close)
                    element.click()
                    allure.attach(f"Нажатие на '{button_name}'.", attachment_type=allure.attachment_type.TEXT)
                except NoSuchElementException:
                    allure.attach(f"Кнопка '{button_name}' отсутствует.", attachment_type=allure.attachment_type.TEXT)
        else:
            element = self.get_first_element(Locators.Button.buttons, button_name)
            if element is None or not self.element_is_visible(element):
                allure.attach(f"Кнопка \'{button_name}\' отсутствует.",
                              attachment_type=allure.attachment_type.TEXT)
                return
            self.element_is_visible(element).click()
            allure.attach(f"Нажатие на кнопку \'{button_name}\'.",
                          attachment_type=allure.attachment_type.TEXT)

    @allure.step("Проверить, что кнопка {button_name} присутствует.")
    def check_button_exists(self, button_name):
        element = self.get_first_element(Locators.Button.buttons, button_name)
        assert self.element_is_visible(element), f"Кнопка \'{button_name}\' отсутствует."
        allure.attach(f"Кнопка \'{button_name}\' присутствует.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Проверить, что кнопка {button_name} отсутствует.")
    def check_button_not_exists(self, button_name):
        element = self.get_first_element(Locators.Button.buttons, button_name)
        assert self.element_is_not_visible(element), f"Кнопка \'{button_name}\' присутствует."
        allure.attach(f"Кнопка \'{button_name}\' отсутствует.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Нажать на ссылку {link_name}.")
    def click_link(self, link_name):
        element = self.get_first_element(Locators.Link.link, link_name)
        assert self.element_is_visible(element), f"Ссылка \'{link_name}\' не найдена."
        self.element_is_visible(element)
        self.element_is_clickable(element).click()
        allure.attach(f"Нажатие на ссылку \'{link_name}\'.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Нажать на кнопку типа 'ссылка' {button_name}.")
    def click_button_type_link(self, button_name):
        element = self.get_first_element(Locators.Button_Type_Link.button_type_link, button_name)
        assert self.element_is_visible(element), f"Кнопка \'{button_name}\' не найдена."
        self.element_is_visible(element).click()
        allure.attach(f"Нажатие на кнопку \'{button_name}\'.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Нажать на кнопку типа 'ссылка' {button_name} под номером {button_number}.")
    def click_button_type_link_by_number(self, button_name, button_number):
        element = self.get_all_elements(Locators.Button_Type_Link.button_type_link, button_name)
        element = element[button_number - 1]
        assert element is not None, f"Кнопка \'{button_name}\' не найдена."
        self.element_is_clickable(element).click()
        allure.attach(f"Нажатие на кнопку \'{button_name}\'.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Проверить, что кнопка типа 'ссылка' {button_name} не присутствует.")
    def check_button_type_link_not_exists(self, button_name):
        time.sleep(1)
        element = self.get_first_element(Locators.Button_Type_Link.button_type_link, button_name)
        assert element is None, f"Кнопка \'{button_name}\' найдена."
        allure.attach(f"Кнопка \'{button_name}\'не присутствует.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Проверить, что кнопка типа 'ссылка' {button_name} присутствует.")
    def check_button_type_link_exists(self, button_name):
        element = self.get_first_element(Locators.Button_Type_Link.button_type_link, button_name)
        assert self.element_is_visible(element) is not None, f"Кнопка \'{button_name}\' не найдена."
        allure.attach(f"Кнопка \'{button_name}\' присутствует.",
                      attachment_type=allure.attachment_type.TEXT)
        return True

    @allure.step("Нажать на кнопку типа 'ссылка' {button_name}, если она присутствует.")
    def if_button_type_link_exists_press(self, button_name):
        element = self.get_first_element(Locators.Button_Type_Link.button_type_link, button_name)
        if element is None or not self.element_is_visible(element):
            allure.attach(f"Кнопка \'{button_name}\' отсутствует.",
                          attachment_type=allure.attachment_type.TEXT)
            return
        self.element_is_visible(element).click()
        allure.attach(f"Нажатие на \'{button_name}\'.",
                      attachment_type=allure.attachment_type.TEXT)

    """
    Шаги с текстом
    """

    @allure.step("Нажать на текст {text}.")
    def click_on_text(self, text):
        element = self.get_first_element(Locators.Text.text, text)
        assert self.element_is_visible(element), f"Текст \'{text}\' не найден."
        self.element_is_clickable(element).click()
        allure.attach(f"Нажатие на текст \'{text}\'.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Нажать на текст {text}.")
    def click_on_text_in_modal_window(self, text):
        window = By.XPATH, Locators.Modal_Window.window
        self.element_is_visible(window)
        element = self.get_first_element_in_window(window, Locators.Text.text, text)
        assert self.element_is_visible(element), f"Текст \'{text}\' не найден."
        self.element_is_visible(element).click()
        allure.attach(f"Нажатие на текст \'{text}\'.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Проверить, что текст {text} присутствует.")
    def check_text_exist(self, text):
        element = self.get_first_element(Locators.Text.text, text)
        assert self.element_is_visible(element), f"Текст \'{text}\' не найден."
        allure.attach(f"Текст \'{text}\' присутствует.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Проверить, что текст {text} отсутствует.")
    def check_text_not_exist(self, text):
        element = self.get_first_element(Locators.Text.text, text)
        if element is not None:
            element = self.element_is_not_visible(element)
            assert element, f"Текст \'{text}\' присутствует."
        allure.attach(f"Текст \'{text}\' отсутствует.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Проверить, что заголовок {heading} присутствует.")
    def check_heading_exists(self, heading):
        element = self.get_first_element(Locators.Heading.heading, heading)
        assert self.element_is_visible(element), f"Заголовок \'{heading}\' не найден."
        allure.attach(f"Заголовок \'{heading}\' присутствует.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Проверить, что заголовок {heading} отсутствует.")
    def check_heading_not_exists(self, heading):
        time.sleep(2)
        element = self.get_first_element(Locators.Heading.heading, heading)
        assert element is None, f"Заголовок \'{heading}\' присутствует."
        allure.attach(f"Заголовок \'{heading}\' отсутствует.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Проверить, что сообщения об ошибке {expected_message} присутствует.")
    def check_error_message(self, expected_message):
        element = self.get_first_element(Locators.Text.errors, expected_message)
        assert self.element_is_visible(element), f"Сообщение об ошибке \'{expected_message}\' не найдено."
        allure.attach(f"Ошибка \'{expected_message}\' присутствует.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Проверить, что сообщения об ошибке {expected_message} отсутствует.")
    def check_no_error_message(self, expected_message):
        element = self.get_first_element(Locators.Text.errors, expected_message)
        assert not self.element_is_visible(element), f"Сообщение об ошибке \'{expected_message}\' найдено."
        allure.attach(f"Ошибка \'{expected_message}\' отсутствует.",
                      attachment_type=allure.attachment_type.TEXT)

    """
    Шаги с выпадающими списками
    """

    @allure.step("Нажать на выпадающий список {list_name} по номеру {list_number}.")
    def click_drop_down_list_by_number(self, list_name, list_number):
        time.sleep(1)
        elements = self.get_all_elements(Locators.Drop_Down_List.list_by_number, list_name)
        assert elements is not None, f"Выпадающий список '{list_name}' не найден."
        element = elements[list_number - 1]
        element.click()
        allure.attach(f"Нажатие на выпадающий список '{list_name}' под номером '{list_number}'.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Нажать на выпадающий список по номеру {list_number}.")
    def click_drop_down_list_by_number_without_name(self, list_number):
        xpath = (By.XPATH, Locators.Drop_Down_List.list_without_name)
        element = self.elements_are_visible(xpath)
        element = element[list_number - 1]
        assert element is not None, f"Выпадающий список под номером \'{list_number}\' не найден."
        element.click()
        allure.attach(f"Нажатие на выпадающий список под номером \'{list_number}\'.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Нажать на выпадающий список {list_name}.")
    def click_drop_down(self, list_name):
        drop_down = self.get_first_element(Locators.Drop_Down_List.list, list_name)
        assert self.element_is_visible(drop_down), f"Выпадающий список \'{list_name}\' не найден."
        self.element_is_visible(drop_down).click()
        allure.attach(f"Нажатие на выпадающий список \'{list_name}\'.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Проверить, что выпадающий список {list_name} присутствует.")
    def check_drop_down_exist(self, list_name):
        drop_down = self.get_first_element(Locators.Drop_Down_List.list, list_name)
        assert self.element_is_visible(drop_down), f"Выпадающий список \'{list_name}\' не найден."
        allure.attach(f"Нажатие на выпадающий список \'{list_name}\'.",
                      attachment_type=allure.attachment_type.TEXT)

    """
    Шаги с чек-боксами
    """

    @allure.step("Выбрать чек-бокс {check_box_name}.")
    def select_check_box(self, check_box_name):
        element = self.get_first_element(Locators.Check_Box.check_box, check_box_name)
        assert self.element_is_visible(element), f"Чек-бокс \'{check_box_name}\' не найден."
        self.element_is_visible(element).click()
        allure.attach(f"Нажатие на чек-бокс \'{check_box_name}\'.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step("Выбрать радио {radio_name}.")
    def select_radio(self, radio_name):
        element = self.get_first_element(Locators.Check_Box.radio, radio_name)
        assert self.element_is_visible(element), f"Радио \'{radio_name}\' не найден."
        self.element_is_visible(element).click()
        allure.attach(f"Нажатие на радио \'{radio_name}\'.",
                      attachment_type=allure.attachment_type.TEXT)

    """
    Шаги с таблицами 
    """

    @allure.step("Проверить, что таблица {table_name} существует.")
    def check_table_exists(self, table_name):
        element = self.get_first_element(Locators.Table.table, table_name)
        assert self.element_is_visible(element), f"Таблица \'{table_name}\' не найдена."
        self.element_is_visible(element).click()
        allure.attach(f"Таблица \'{table_name}\' найдена.",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.step(
        "Проверить, что в таблице {table_name}, в столбце {column_name}, в строке под номером {row_number} присутствует текст {text}.")
    def check_text_present_in_table_by_column_name_row_number(self, table_name, column_name, row_number, text):
        if table_name == '':
            column = Locators.Table.column_name.format(row_number, column_name, column_name)
            table = By.XPATH, Locators.Table.table
            self.element_is_visible(table)
            xpath = Locators.Table.table + column
            cell = self.driver.find_element(By.XPATH, xpath)
            txt = cell.text
            assert text in txt, f"В ячейке {column_name} нет текста {text}."
            allure.attach(f"Таблица \'{table_name}\' найдена.",
                          attachment_type=allure.attachment_type.TEXT)
        else:
            column = Locators.Table.column_name.format(row_number, column_name)
            table = self.get_first_element(Locators.Table.table, table_name)
            self.element_is_visible(table)
            cell = self.driver.find_element(By.XPATH, f"{table[1]}{column}")
            txt = cell.text
            assert text in txt, f"В ячейке {column_name} нет текста {text}."
            allure.attach(f"Таблица \'{table_name}\' найдена.",
                          attachment_type=allure.attachment_type.TEXT)

    @allure.step(
        "Проверить, что в таблице {table_name}, в столбце {column_number}, в строке под номером {row_number} присутствует текст {text}.")
    def check_text_present_in_table_by_column_number_row_number(self, table_name, column_number, row_number, text):
        if table_name == '':
            column = Locators.Table.column_number.format(row_number, column_number)
            table = By.XPATH, f"{Locators.Table.table}{column}"
            self.element_is_visible(table)
            cell = self.driver.find_element(By.XPATH, f"{Locators.Table.table}{column}")
            txt = cell.text
            assert text in txt, f"В ячейке {column_number} нет текста {text}."
            allure.attach(f"Таблица \'{table_name}\' найдена.",
                          attachment_type=allure.attachment_type.TEXT)
        else:
            column = Locators.Table.column_number.format(row_number, column_number)
            table = self.get_first_element(Locators.Table.table, table_name)
            self.element_is_visible(table)
            cell = self.driver.find_element(By.XPATH, f"{table[1]}{column}")
            txt = cell.text
            assert text in txt, f"В ячейке {column_number} нет текста {text}."
            allure.attach(f"Таблица \'{table_name}\' найдена.",
                          attachment_type=allure.attachment_type.TEXT)

    """
    Шаги использованием перетаскивания 
    """

    @allure.step("Изменить точку на карте.")
    def map_edit_point(self):
        xpath = (By.XPATH, Locators.Map.map_point)
        element = self.element_is_visible(xpath)
        style1 = element.get_attribute("style")
        style_transform1 = re.search(r'transform:\s*(.*?);', style1).group(1)

        actions = webdriver.ActionChains(self.driver)

        actions.click_and_hold(element).move_by_offset(10, 10).release(element).perform()

        element = self.driver.find_element(By.XPATH, Locators.Map.map_point)
        style2 = element.get_attribute("style")
        style_transform2 = re.search(r'transform:\s*(.*?);', style2).group(1)
        assert style_transform1 != style_transform2, "Координаты не изменились"

    @allure.step("Изменить точку на карте")
    def map_edit_point1(self, xx, yy):
        # Ожидание, чтобы убедиться, что элемент появился на странице
        time.sleep(3)
        xpath = (By.XPATH, Locators.Map.map_point)
        element = self.element_is_visible(xpath)

        action_chains = webdriver.ActionChains(self.driver)
        style1 = element.get_attribute("style")
        style_transform1 = re.search(r'transform:\s*(.*?);', style1).group(1)

        # Перемещение элемента на заданные координаты
        action_chains.drag_and_drop_by_offset(element, 50, 50).perform()
        action_chains.click_and_hold(element).move_by_offset(xx, yy).release(element).perform()
        action_chains.perform()
        # click_and_hold(element).move_by_offset(xx, yy).release(element).perform()
        time.sleep(3)
        action_chains.context_click(element).perform()

        time.sleep(1)

        # Повторное получение элемента после перемещения
        element = self.element_is_visible(xpath)
        style2 = element.get_attribute("style")
        style_transform2 = re.search(r'transform:\s*(.*?);', style2).group(1)

        # Проверка изменения координат
        assert style_transform1 != style_transform2, "Координаты не изменились"

    @allure.step("Поменять местами два адреса")
    def swap_point_A_and_point_B(self, point1, point2):
        element = self.driver.find_elements(By.XPATH, Locators.Map.edit_order)
        action_chains = webdriver.ActionChains(self.driver)
        action_chains.drag_and_drop(element[point1 - 1], element[point2 - 1]).perform()
        # assert style_transform1 != style_transform2, "Координаты не изменились"

    @allure.step("Установить ползунок бонусов на отметку - {bonus_amount}.")
    def install_bonuses(self, bonus_amount):
        slider = By.XPATH, Locators.Elements.bonus_slider
        self.element_is_visible(slider).click()
        for _ in range(bonus_amount):
            # Зажимаем стрелочку вправо
            pyautogui.keyDown('right')
            pyautogui.keyUp('right')
            time.sleep(0.1)

    """
    Шаги с различными элементами
    """

    @allure.step("Проверить, что элемент {element_name} присутствует")
    def check_element_exist(self, element_name):
        if element_name == 'Карта':
            xpath = By.XPATH, Locators.Map.map
            element = self.element_is_visible(xpath)
            assert element is not None, f"Элемент {element_name} не найден."

    @allure.step("Получить текст у элемента")
    def get_text_element(self, element_name, number=None):
        if element_name == 'дата':
            element = By.XPATH, "//a[@class='ordered_when s_datepicker a_sc']"
            element = self.element_is_visible(element)
            text = element.text
            return text
        if element_name == 'номер':
            element = self.get_first_element(Locators.Link.link, "Новый")
            actual_value = self.driver.find_element(By.XPATH, element[1] + "/parent::*").get_attribute("class")
            if actual_value == "active":
                element = By.XPATH, "//a[@class='ot_open']"
                element = self.elements_are_visible(element)
                text = element[number - 1].text
                return text
            else:
                element = By.XPATH, "//*[contains(@id,'pre')]/td[1]/a"
                element = self.elements_are_visible(element)
                text = element[number - 1].text
                return text

    @allure.step("Нажать на элемент {button_name} по номеру {number}.")
    def click_element_by_number(self, button_name, number):
        if button_name == "Удалить":
            if self.page_loaded():
                xpath = By.XPATH, Locators.Button.delete_item
                elements = self.elements_are_visible(xpath)
                element = elements[number - 1]
                assert element is not None, f"Элемент \'{button_name}\' не найден."
                self.element_is_clickable(element).click()
                allure.attach(f"Нажатие на элемент \'{button_name}\'.",
                              attachment_type=allure.attachment_type.TEXT)

    """
    Вспомогательные шаги
    """

    @allure.step("Подождать {time_wait} секунд.")
    def wait(self, time_wait):
        time.sleep(time_wait)


    @allure.step("Удалить все заказы")
    def delete_all_orders(self):
        elements = By.XPATH, Locators.Button.button_edit
        try:
            elements = self.elements_are_visible(elements, 5)
        except TimeoutException:
            print("Нет кнопки редактировать")
            elements = None
        if elements is not None:
            for i in range(len(elements)):
                self.driver.find_element(By.XPATH, Locators.Button.button_edit).click()
                time.sleep(3)
                self.click_drop_down("Действие с заказом")
                self.click_on_text("Отменить заказ")
                self.click_button("Сохранить")
                self.click_drop_down("Действие с заказом")
                self.click_on_text("Удалить заказ")
                self.click_button("Сохранить")
                self.click_button("Закрыть")
                time.sleep(2)

    @allure.step("Удалить все заказы")
    def delete_all_orders_dispatcher(self):
        elements = By.XPATH, Locators.Button.button_edit
        try:
            elements = self.elements_are_visible(elements, 5)
        except TimeoutException:
            print("Нет кнопки редактировать")
            elements = None
        if elements is not None:
            for i in range(len(elements)):
                self.driver.find_element(By.XPATH, Locators.Button.button_edit).click()
                time.sleep(3)
                self.click_drop_down("Действие с заказом")
                self.click_on_text("Отменить заказ")
                self.click_button("Сохранить")
                self.click_drop_down("Действие с заказом")
                self.click_on_text("Удалить заказ")
                self.click_button("Сохранить")
                self.if_button_type_link_exists_press("Назад")
                self.if_button_exists_press("Закрыть")
                time.sleep(2)

    @allure.step("Сгенерировать номер телефона")
    def random_phone_number(self):
        """Функция для генерации номера телефона."""
        phone_number = '7'
        for x in range(10):
            phone_number += str(random.randint(0, 9))
        return phone_number

    @allure.step("Сгенерировать почту")
    def generate_random_email(self):
        domains = ['.com', '.net', '.org', '.info']  # список возможных доменов
        email_length = random.randint(5, 10)  # случайная длина имени почты
        domain = random.choice(domains)  # случайный выбор домена

        # генерация случайного адреса почты
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=email_length))
        email = username + '@mail' + domain
        return email

    @allure.step("Сгенерировать имя")
    def generate_random_name(self):
        # Список имен и фамилий для генерации
        names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
        surnames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown']

        # Выбор случайного имени и фамилии
        random_name = random.choice(names)
        random_surname = random.choice(surnames)

        return random_name + ' ' + random_surname

    @allure.step("Сгенерировать адрес")
    def generate_random_address(self):
        streets = ['Sunset Boulevard', 'Main Street', 'Maple Avenue', 'Park Road', 'Broadway']
        cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']
        numbers = list(range(1, 1001))  # Номера домов от 1 до 1000

        street = random.choice(streets)
        number = random.choice(numbers)
        city = random.choice(cities)
        return f"{number} {street}, {city}"


    """
    Проверка на js ошибки
    """

    @allure.step("Проверить на js ошибки.")
    def check_js_errors(self):
        logs = self.driver.get_log('browser')
        js_errors = [log['message'] for log in logs if log['level'] == 'SEVERE' and 'Error' in log['message']]
        assert not js_errors, f"JavaScript errors found: {js_errors}"
        allure.attach("Ошибок на странице не найдено.",
                      attachment_type=allure.attachment_type.TEXT)

    """
    Шаги с календарем или датой
    """

    @allure.step("Получить текущий день")
    def get_current_day(self):
        current_day = datetime.datetime.now().day
        return current_day

    @allure.step("Выбрать день в календаре {day}")
    def set_day(self, day):
        current_day = self.get_current_day()
        xpath = "//td//a[.=\'{}\' and not(ancestor::*[@style='display: none;'])]"
        if day == 'сегодня':
            xpath = xpath.format(current_day)
            current_day = self.driver.find_element(By.XPATH, xpath)
            current_day.click()
        elif day == 'вчера':
            if current_day == 1:
                xpath_back = "//span[.='<Пред' and not(ancestor::*[@style='display: none;'])]"
                yesterday_element = self.driver.find_element(By.XPATH, xpath_back)
                yesterday_element.click()
                previous_day_element = self.driver.find_elements(By.XPATH,
                                                                 "//td//a[contains(@class,'ui-state-default') and not(ancestor::*[@style='display: none;'])]")
                xpath = "//td//a[.=\'{}\' and not(ancestor::*[@style='display: none;'])]"
                xpath = xpath.format(len(previous_day_element))
                yesterday = self.driver.find_element(By.XPATH, xpath)
                yesterday.click()
            else:
                xpath = xpath.format(current_day - 1)
                yesterday = self.driver.find_element(By.XPATH, xpath)
                yesterday.click()
        elif day == 'завтра':
            previous_day_element = self.driver.find_elements(By.XPATH,
                                                             "//td//a[contains(@class,'ui-state-default') and not(ancestor::*[@style='display: none;'])]")
            if len(previous_day_element) == current_day:
                xpath_next = self.driver.find_element(By.XPATH,
                                                      "//span[.='След>' and not(ancestor::*[@style='display: none;'])]")
                xpath_next.click()
                xpath = "//td//a[.=\'{}\' and not(ancestor::*[@style='display: none;'])]"
                xpath = xpath.format(1)
                tomorrow = self.driver.find_element(By.XPATH, xpath)
                tomorrow.click()
            else:
                xpath = xpath.format(current_day + 1)
                tomorrow = self.driver.find_element(By.XPATH, xpath)
                tomorrow.click()

    @allure.step("Отредактировать дату {date_string}")
    def convert_date(self, date_string):
        # Устанавливаем локаль для русского языка
        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
        # locale.setlocale(locale.LC_TIME, locale.getlocale())

        date_object = datetime.datetime.strptime(date_string, '%d.%m.%Y %H:%M')

        # Извлекаем день, месяц и год
        day = date_object.day
        month = date_object.month
        year = date_object.year

        # Добавляем ведущий ноль, если день равен от 1 до 9
        if 1 <= day <= 9:
            day = f'0{day}'

        # Используем модуль calendar для получения названия месяца
        month_name = calendar.month_name[month]
        if month_name.endswith("я"):
            pass
        elif month_name.endswith("ь"):
            month_name = month_name[:-1] + "я"
        elif month_name.endswith("й"):
            month_name = month_name[:-1] + "я"
        else:
            month_name += "а"

        # Формируем строку с датой и временем
        formatted_date = f'{day} {month_name.lower()} {year} г., {date_object.strftime("%H:%M")}'

        return formatted_date
