from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..common.common_selectors import *


def test_go_from_logged_personal_account_to_constructor_pass(login, driver):
    # Переходим в Личный кабинет
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, CONSTRUCTOR_LINK)))
    # Переходим в Конструктор по ссылке Конструктор
    driver.find_element(By.XPATH, CONSTRUCTOR_LINK).click()
    # Убеждаемся, что это действительно Конструктор - присутствует заголовок "Соберите бургер"
    element = driver.find_element(By.XPATH, MAKE_BURGER_HEADER).text
    assert element == "Соберите бургер"


def test_go_from_logged_personal_account_to_logo_pass(login, driver):
    # Переходим в Личный кабинет
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    # Переходим в Конструктор по ссылке на логотип
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LOGO_LINK)))
    driver.find_element(By.XPATH, LOGO_LINK).click()
    # Убеждаемся, что это действительно Конструктор - присутствует заголовок "Соберите бургер"
    element = driver.find_element(By.XPATH, MAKE_BURGER_HEADER).text
    assert element == "Соберите бургер"


def test_go_from_unlogged_personal_account_to_constructor_pass(driver):
    # Переходим в Личный кабинет, не логинясь
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, CONSTRUCTOR_LINK)))
    # Переходим в Конструктор по ссылке Конструктор
    driver.find_element(By.XPATH, CONSTRUCTOR_LINK).click()
    # Убеждаемся, что это действительно Конструктор - присутствует заголовок "Соберите бургер"
    element = driver.find_element(By.XPATH, MAKE_BURGER_HEADER).text
    assert element == "Соберите бургер"


def test_go_from_unlogged_personal_account_to_logo_pass(driver):
    # Переходим в Личный кабинет, не логинясь
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LOGO_LINK)))
    # Переходим в Конструктор по ссылке на логотип
    driver.find_element(By.XPATH, LOGO_LINK).click()
    # Убеждаемся, что это действительно Конструктор - присутствует заголовок "Соберите бургер"
    element = driver.find_element(By.XPATH, MAKE_BURGER_HEADER).text
    assert element == "Соберите бургер"