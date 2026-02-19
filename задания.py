import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser_function():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("quit browser for test..")
    browser.quit()


class TestMainPage2:
    def test_guest_should_see_login_link(self, browser_function):
        browser_function.get(link)
        browser_function.find_element(By.CSS_SELECTOR, "#login_link")

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("quit browser for test..")
    browser.quit()

class TestMainPage:
    def test_element_not_exist(self, browser):
        browser.get(link)
        # Пытаемся найти несуществующий элемент
        browser.find_element(By.CSS_SELECTOR, "#element_which_does_not_exist")