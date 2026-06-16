from uuid import uuid4

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import (
    BUTTON_CREATE_ACCOUNT,
    BUTTON_LOGIN_REGISTRATION,
    BUTTON_NO_ACCOUNT,
    BUTTON_PROFILE,
    FIELD_EMAIL,
    FIELD_PASSWORD,
    FIELD_REPEAT_PASSWORD,
    USERNAME,
)


class TestUserRegistration:
    def test_user_registration(self, driver):
        # Нажать кнопку «Вход и регистрация».
        driver.find_element(By.XPATH, BUTTON_LOGIN_REGISTRATION).click()
        # Нажать кнопку «Нет аккаунта».
        driver.find_element(By.XPATH, BUTTON_NO_ACCOUNT).click()
        # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
        password = "Qwerty123!"
        driver.find_element(By.XPATH, FIELD_EMAIL).send_keys(f"test_user{uuid4()}@ya.ru")
        driver.find_element(By.XPATH, FIELD_PASSWORD).send_keys(password)
        driver.find_element(By.XPATH, FIELD_REPEAT_PASSWORD).send_keys(password)
        driver.find_element(By.XPATH, BUTTON_CREATE_ACCOUNT).click()

        # Проверить: переход выполнен, в правом верхнем углу отображаются аватар и имя User.
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, BUTTON_PROFILE)))
        assert driver.find_element(By.XPATH, USERNAME).text == "User."
        assert driver.find_element(By.XPATH, BUTTON_PROFILE).is_displayed() is True
