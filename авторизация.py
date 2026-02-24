import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_stepik_login(browser):
    # Загружаем логин и пароль из .env
    load_dotenv()
    login = os.getenv("STEPIC_LOGIN")
    password = os.getenv("STEPIC_PASSWORD")

    # Открываем урок
    browser.get("https://stepik.org/lesson/236895/step/1")

    # Нажимаем кнопку "Войти"
    login_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
    )
    login_button.click()

    # Вводим логин
    email_field = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.NAME, "login"))
    )
    email_field.send_keys(login)

    # Вводим пароль
    password_field = browser.find_element(By.NAME, "password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    # Ждём исчезновения поп-апа авторизации
    WebDriverWait(browser, 15).until(
        EC.invisibility_of_element((By.CLASS_NAME, "modal-dialog"))
    )

    # Проверяем, что пользователь авторизован (например, есть аватар)
    avatar = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img.navbar__profile-img"))
    )
    assert avatar is not None
