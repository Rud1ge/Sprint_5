from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import (
    BUTTON_CREATE_ACCOUNT,
    BUTTON_LOGIN_REGISTRATION,
    BUTTON_NO_ACCOUNT,
    FIELD_EMAIL,
    FIELD_ERROR_EMAIL,
    FIELD_ERROR_PASSWORD,
    FIELD_ERROR_REPEAT_PASSWORD,
    FIELD_PASSWORD,
    FIELD_REPEAT_PASSWORD,
    TEXT_ERROR,
)


def test_user_registration_existing_user(driver, existing_user_credentials):
    existing_email, existing_password = existing_user_credentials

    # Нажать кнопку «Вход и регистрация»
    driver.find_element(By.XPATH, BUTTON_LOGIN_REGISTRATION).click()
    # Нажать кнопку «Нет аккаунта»
    driver.find_element(By.XPATH, BUTTON_NO_ACCOUNT).click()
    # Заполнить все поля формы регистрации данными уже существующего пользователя и нажать «Создать аккаунт»
    driver.find_element(By.XPATH, FIELD_EMAIL).send_keys(existing_email)
    driver.find_element(By.XPATH, FIELD_PASSWORD).send_keys(existing_password)
    driver.find_element(By.XPATH, FIELD_REPEAT_PASSWORD).send_keys(existing_password)
    driver.find_element(By.XPATH, BUTTON_CREATE_ACCOUNT).click()

    # Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка»
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, FIELD_ERROR_EMAIL)))
    assert driver.find_element(By.XPATH, FIELD_ERROR_PASSWORD)
    assert driver.find_element(By.XPATH, FIELD_ERROR_REPEAT_PASSWORD)
    assert driver.find_element(By.XPATH, TEXT_ERROR)
