import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

# Загружаем логин и пароль из .env
load_dotenv()
LOGIN = os.getenv("STEPIC_LOGIN")
PASSWORD = os.getenv("STEPIC_PASSWORD")

urls = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.parametrize('link', urls)
def test_feedback_correct(browser, link):
    browser.get(link)

    # Авторизация
    browser.find_element(By.CSS_SELECTOR, "a.navbar__auth_login").click()
    browser.find_element(By.NAME, "login").send_keys(LOGIN)
    browser.find_element(By.NAME, "password").send_keys(PASSWORD)
    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

    # Ждём поле для ввода
    input_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
    )

    # Сразу вычисляем и вводим ответ
    answer = math.log(int(time.time()))
    input_field.clear()
    input_field.send_keys(str(answer))

    # Ждём кнопку и сразу кликаем (без сохранения в переменную)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    ).click()

    # Ждём появления фидбека
    feedback = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    ).text

    # Проверка
    try:
        assert feedback == "Correct!", f"Опциональный фидбек отличается: ожидалось 'Correct!', получено '{feedback}'"
    except AssertionError:
        # Сохраняем неожиданный фидбек в файл
        with open("alien_message.txt", "a", encoding="utf-8") as f:
            f.write(feedback + "\n")
        raise



