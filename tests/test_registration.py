from selenium.webdriver.common.by import By
from ..common.common_procedures import generate_login, generate_password
from ..common.common_selectors import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_correct_registration(driver):
    # Переходим в Личный кабинет, заходим в форму регистрации
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(By.XPATH, REGISTRATION_LINK).click()
    # Заполняем поле имя
    driver.find_element(By.XPATH, NAME_FIELD).send_keys('Елена')
    # Генерируем логин и пароль
    login = generate_login()
    password = generate_password(6)
    # Заполняем поля логин и пароль, жмем "зарегистрироваться", ждем, пока появится форма входа
    driver.find_element(By.XPATH, EMAIL_FIELD).send_keys(login)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(password)
    driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ENTER_BUTTON)))
    # В форме входа вводим логин и пароль только что зарегистрированного пользователя, жмем "Войти"
    driver.find_element(By.XPATH, EMAIL_FIELD).send_keys(login)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(password)
    driver.find_element(By.XPATH, ENTER_BUTTON).click()
    # Переходим в Личный кабинет, ждем, пока будет видно поле Логин
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_FIELD)))
    # Проверяем, что в поле Логин - тот логин, под которым мы зарегистрировались и вошли
    element = driver.find_element(By.XPATH, LOGIN_FIELD).get_attribute("value")
    assert element == login


def test_registration_password_shorter_6_symbols_FAIL(driver):
    # Входим в Личный кабинет, переходим по ссылке Зарегистрироваться, заполняем поле "Имя"
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(By.XPATH, REGISTRATION_LINK).click()
    driver.find_element(By.XPATH, NAME_FIELD).send_keys('Елена')
    # Генерируем корректный логин
    login = generate_login()
    # Генерируем слишком короткий пароль
    password = generate_password(5)
    # Заполняем поля формы регистрации, жмем кнопку "Зарегистрироваться"
    driver.find_element(By.XPATH, EMAIL_FIELD).send_keys(login)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(password)
    driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()
    # Проверяем текст появившегося сообщения об ошибке
    element = driver.find_element(By.CLASS_NAME, ERROR_STRING).text
    assert element == "Некорректный пароль"
