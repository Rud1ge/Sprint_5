from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import (
    BUTTON_LOGIN,
    BUTTON_LOGIN_REGISTRATION,
    BUTTON_PROFILE,
    FIELD_EMAIL,
    FIELD_PASSWORD,
    USERNAME,
)


class TestUserLogin:
    def test_user_login(self, driver, existing_user_credentials):
        email, password = existing_user_credentials
        # Нажать кнопку «Вход и регистрация».
        driver.find_element(By.XPATH, BUTTON_LOGIN_REGISTRATION).click()
        # Заполнить поля формы авторизации и нажать кнопку «Войти».
        driver.find_element(By.XPATH, FIELD_EMAIL).send_keys(email)
        driver.find_element(By.XPATH, FIELD_PASSWORD).send_keys(password)
        driver.find_element(By.XPATH, BUTTON_LOGIN).click()

        # Проверить: в правом верхнем углу отображаются аватар и имя User.
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, BUTTON_PROFILE)))
        assert driver.find_element(By.XPATH, BUTTON_PROFILE).is_displayed() is True
        assert driver.find_element(By.XPATH, USERNAME).text == "User."
