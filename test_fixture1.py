from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")




import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

# Фикстура для браузера с областью видимости "class"
#@pytest.fixture(scope="class")
#def browser_class():
    #print("\nstart browser for test suite..")
    #browser = webdriver.Chrome()
    #yield browser
    #print("quit browser for test suite..")
    #browser.quit()

# Фикстура для браузера с областью видимости "function" (по умолчанию)
@pytest.fixture
def browser_function():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("quit browser for test..")
    browser.quit()


# Используем фикстуру с областью видимости "class"
#class TestMainPage1:
    #def test_guest_should_see_login_link(self, browser_class):
        #browser_class.get(link)
        #browser_class.find_element(By.CSS_SELECTOR, "#login_link")

    #def test_guest_should_see_basket_link_on_the_main_page(self, browser_class):
        #browser_class.get(link)
        #browser_class.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


# Используем фикстуру с областью видимости "function"
class TestMainPage2:
    def test_guest_should_see_login_link(self, browser_function):
        browser_function.get(link)
        browser_function.find_element(By.CSS_SELECTOR, "#login_link")

    #def test_guest_should_see_basket_link_on_the_main_page(self, browser_function):
        #browser_function.get(link)
        #browser_function.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")