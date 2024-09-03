from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from common.common_selectors import *


def test_navigate_to_sauces_unlogged_constructor_pass(driver):
    # Не логинимся. Переходим в Личный Кабинет, оттуда - в Конструктор
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, CONSTRUCTOR_LINK)))
    driver.find_element(By.XPATH, CONSTRUCTOR_LINK).click()
    # Переходим по ссылке "Соусы"
    driver.find_element(By.XPATH, SAUCE_LINK).click()
    # Убеждаемся, что в Конструкторе активная секция - Соусы
    element = driver.find_element(By.XPATH, ACTIVE_SECTION).text
    assert element == 'Соусы'


def test_navigate_to_bread_unlogged_constructor_pass(driver):
    # Не логинимся. Переходим в Личный кабинет, оттуда - в конструктор
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, CONSTRUCTOR_LINK)))
    driver.find_element(By.XPATH, CONSTRUCTOR_LINK).click()
    # Переходим по ссылке "Соусы", потом - по ссылке "Булки"
    driver.find_element(By.XPATH, SAUCE_LINK).click()
    driver.find_element(By.XPATH, BREAD_LINK).click()
    # Убеждаемся, что активная секция в Конструкторе - "Булки"
    element = driver.find_element(By.XPATH, ACTIVE_SECTION).text
    assert element == 'Булки'


def test_navigate_to_filling_unlogged_constructor_pass(driver):
    # Не логинимся. Переходим в Личный кабинет, оттуда - в Конструктор
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, CONSTRUCTOR_LINK)))
    driver.find_element(By.XPATH, CONSTRUCTOR_LINK).click()
    # Жмем на ссылку "Начинки"
    driver.find_element(By.XPATH, FILLER_LINK).click()
    # Убеждаемся, что активная секция конструктора - "Начинки"
    element = driver.find_element(By.XPATH, ACTIVE_SECTION).text
    assert element == 'Начинки'


def test_navigate_to_sauces_logged_constructor_pass(login, driver):
    # Переходим в Личный кабинет, оттуда - в Конструктор
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, CONSTRUCTOR_LINK)))
    driver.find_element(By.XPATH, CONSTRUCTOR_LINK).click()
    # Переходим по ссылке "Соусы"
    driver.find_element(By.XPATH, SAUCE_LINK).click()
    # Убеждаемся, что в Конструкторе активная секция - Соусы
    element = driver.find_element(By.XPATH, ACTIVE_SECTION).text
    assert element == 'Соусы'


def test_navigate_to_bread_logged_constructor_pass(login, driver):
    # Переходим в Личный кабинет, оттуда - в Конструктор
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, CONSTRUCTOR_LINK)))
    driver.find_element(By.XPATH, CONSTRUCTOR_LINK).click()
    # Жмем на ссылку "Соусы", потом - на ссылку "Булки"
    driver.find_element(By.XPATH, SAUCE_LINK).click()
    driver.find_element(By.XPATH, BREAD_LINK).click()
    # Убеждаемся, что активная секция в Конструкторе - "Булки"
    element = driver.find_element(By.XPATH, ACTIVE_SECTION).text
    assert element == 'Булки'


def test_navigate_to_filling_logged_constructor_pass(login, driver):
    # Переходим в Личный кабинет, оттуда - в Конструктор
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, CONSTRUCTOR_LINK)))
    driver.find_element(By.XPATH, CONSTRUCTOR_LINK).click()
    # Жмем на ссылку "Начинки"
    driver.find_element(By.XPATH, FILLER_LINK).click()
    # Убеждаемся, что активная секция конструктора - "Начинки"
    element = driver.find_element(By.XPATH, ACTIVE_SECTION).text
    assert element == 'Начинки'


