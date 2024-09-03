from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..common.common_selectors import *


def test_open_personal_account_without_login_pass(driver):
    # Переходим в Личный кабинет, не логинясь
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    # Проверяем, что вместо личного кабинета - форма входа с заголовком "Вход"
    element = driver.find_element(By.XPATH, ENTER_HEADER).text
    assert element == 'Вход'


def test_open_personal_account_after_login_pass(login, driver):
    # Переходим в Личный кабинет
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, PROFILE_LINK)))
    # Проверяем, что перед нами Личный кабинет - присутствует ссылка "Профиль"
    element = driver.find_element(By.CLASS_NAME, PROFILE_LINK).text
    assert element == 'Профиль'