from uuid import uuid4

from locators import (
    BUTTON_CREATE_ACCOUNT,
    BUTTON_LOGIN_REGISTRATION,
    BUTTON_NO_ACCOUNT,
    BUTTON_PROFILE,
    FIELD_EMAIL,
    USERNAME,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_user_registration(driver):
    # Нажать кнопку «Вход и регистрация»
    driver.find_element(By.XPATH, BUTTON_LOGIN_REGISTRATION).click()

    # Нажать кнопку «Нет аккаунта»
    driver.find_element(By.XPATH, BUTTON_NO_ACCOUNT).click()

    # Заполнить поле Email формы регистрации и нажать кнопку «Создать аккаунт»
    driver.find_element(By.XPATH, FIELD_EMAIL).send_keys(f"test_user{uuid4()}@ya.ru")
    driver.find_element(By.XPATH, BUTTON_CREATE_ACCOUNT).click()

    # Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, BUTTON_PROFILE))
    )
    assert driver.current_url == "https://qa-desk.education-services.ru/regiatration"
    assert driver.find_element(By.XPATH, BUTTON_PROFILE)
    assert driver.find_element(By.XPATH, USERNAME).text == "User."
