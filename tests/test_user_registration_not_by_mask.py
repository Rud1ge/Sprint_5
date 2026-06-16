from uuid import uuid4

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
    TEXT_ERROR,
)


def test_user_registration_not_by_mask(driver):
    # Нажать кнопку «Вход и регистрация»
    driver.find_element(By.XPATH, BUTTON_LOGIN_REGISTRATION).click()
    # Нажать кнопку «Нет аккаунта»
    driver.find_element(By.XPATH, BUTTON_NO_ACCOUNT).click()
    # Заполнить поле Email формы регистрации и нажать кнопку «Создать аккаунт»
    driver.find_element(By.XPATH, FIELD_EMAIL).send_keys(f"{uuid4()}")
    driver.find_element(By.XPATH, BUTTON_CREATE_ACCOUNT).click()

    # Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка»
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, FIELD_ERROR_EMAIL)))
    assert driver.find_element(By.XPATH, FIELD_ERROR_PASSWORD)
    assert driver.find_element(By.XPATH, FIELD_ERROR_REPEAT_PASSWORD)
    assert driver.find_element(By.XPATH, TEXT_ERROR)
