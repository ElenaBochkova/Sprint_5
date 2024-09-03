from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..common.common_selectors import *


def test_login_through_main_page_pass(generated_user, driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    # Переходим по ссылке "Войти в аккаунт" и заполняем данные логином и паролем сгенерованного в фикстуре пользователя
    driver.find_element(By.XPATH, ENTER_ACCOUNT_BUTTON).click()
    driver.find_element(By.XPATH, EMAIL_FIELD).send_keys(generated_user.login)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(generated_user.password)
    # Жмем по кнопке "Войти"
    driver.find_element(By.XPATH, ENTER_BUTTON).click()
    # Переходим в Личный кабинет
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_FIELD)))
    # Убеждаемся, что логин пользователя в Личном кабинете - именно тот, под которым мы логинились
    element = driver.find_element(By.XPATH, LOGIN_FIELD).get_attribute("value")
    assert element == generated_user.login


def test_login_through_personal_account_pass(generated_user, driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    # Переходим в Личный Кабинет и заполняем данные логином и паролем сгенерованного в фикстуре пользователя
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(By.XPATH, EMAIL_FIELD).send_keys(generated_user.login)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(generated_user.password)
    # Жмем по кнопке "Войти"
    driver.find_element(By.XPATH, ENTER_BUTTON).click()
    # Переходим в Личный кабинет
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_FIELD)))
    # Убеждаемся, что логин пользователя в Личном кабинете - именно тот, под которым мы логинились
    element = driver.find_element(By.XPATH, LOGIN_FIELD).get_attribute("value")
    assert element == generated_user.login


def test_login_through_link_in_registration_form_pass(generated_user, driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    # Переходим в Личный Кабинет, оттуда - по ссылке "Зарегистрироваться", оттуда - по ссылке "Вход"
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(By.XPATH, REGISTRATION_LINK).click()
    driver.find_element(By.XPATH, ENTER_LINK).click()
    # заполняем данные логином и паролем сгенерованного в фикстуре пользователя
    driver.find_element(By.XPATH, EMAIL_FIELD).send_keys(generated_user.login)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(generated_user.password)
    # Жмем по кнопке "Войти"
    driver.find_element(By.XPATH, ENTER_BUTTON).click()
    # Переходим в Личный кабинет
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_FIELD)))
    # Убеждаемся, что логин пользователя в Личном кабинете - именно тот, под которым мы логинились
    element = driver.find_element(By.XPATH, LOGIN_FIELD).get_attribute("value")
    assert element == generated_user.login


def test_login_through_link_in_password_recovery_form_pass(generated_user, driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    # Переходим в Личный кабинет, оттуда по ссылке "Восстановить пароль", оттуда - по ссылке "Войти"
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(By.XPATH, RESTORE_PASSWORD_LINK).click()
    driver.find_element(By.XPATH, ENTER_LINK).click()
    # заполняем данные логином и паролем сгенерованного в фикстуре пользователя
    driver.find_element(By.XPATH, EMAIL_FIELD).send_keys(generated_user.login)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(generated_user.password)
    # Жмем по кнопке "Войти"
    driver.find_element(By.XPATH, ENTER_BUTTON).click()
    # Переходим в Личный кабинет
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_FIELD)))
    # Убеждаемся, что логин пользователя в Личном кабинете - именно тот, под которым мы логинились
    element = driver.find_element(By.XPATH, LOGIN_FIELD).get_attribute("value")
    assert element == generated_user.login