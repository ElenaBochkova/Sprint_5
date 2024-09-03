import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from ..common.common_procedures import generate_login, generate_password
from ..common.common_user_class import User
from ..common.common_selectors import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def generated_user(driver):
    # Переходим в Личный кабинет, кликаем по ссылке "Зарегистрироваться
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(By.XPATH, REGISTRATION_LINK).click()
    # Заполняем поле "Имя"
    driver.find_element(By.XPATH, NAME_FIELD).send_keys('Елена')
    # Генерируем логин и пароль длиной 6 символов
    login = generate_login()
    password = generate_password(6)
    # Создаем пользователя со сгенерированными логином и паролем
    user = User(login, password)
    # Заполняем поля Логин и пароль, жмем на кнопку Регистрации
    driver.find_element(By.XPATH, EMAIL_FIELD).send_keys(login)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(password)
    driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ENTER_BUTTON)))
    # Возвращаем в функцию зарегистрированного пользователя
    return user


@pytest.fixture(scope="function")
def login(generated_user, driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    #Логинимся через кнопку "Войти в аккаунт" на главной странице
    driver.find_element(By.XPATH, ENTER_ACCOUNT_BUTTON).click()
    driver.find_element(By.XPATH, EMAIL_FIELD).send_keys(generated_user.login)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(
        generated_user.password)
    driver.find_element(By.XPATH, ENTER_BUTTON).click()
    # Возвращаем сгенерированного пользователя, может понадобиться
    return generated_user

