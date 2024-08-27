from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..common.common_selectors import *


def test_open_personal_account_after_login_pass(login, driver):
    # Переходим в личный кабинет и ждем, пока он прогрузится
    driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, PROFILE_LINK)))
    # Жмем по кнопке "Выход"
    driver.find_element(By.XPATH, QUIT_BUTTON).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ENTER_HEADER)))
    # Проверяем, что на экране появилась форма входа - присутствует заголовок "Вход"
    element = driver.find_element(By.XPATH, ENTER_HEADER).text
    assert element == 'Вход'