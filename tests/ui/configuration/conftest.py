import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/text-box")
    yield driver
    driver.quit()
