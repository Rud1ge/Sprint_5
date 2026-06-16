from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import (
    BUTTON_LOGIN,
    BUTTON_LOGIN_REGISTRATION,
    BUTTON_LOGOUT,
    BUTTON_PROFILE,
    FIELD_EMAIL,
    FIELD_PASSWORD,
    USERNAME,
)


class TestUserLogout:
    def test_user_logout(self, driver, existing_user_credentials):
        email, password = existing_user_credentials
        # Авторизоваться под заранее созданным пользователем.
        driver.find_element(By.XPATH, BUTTON_LOGIN_REGISTRATION).click()
        driver.find_element(By.XPATH, FIELD_EMAIL).send_keys(email)
        driver.find_element(By.XPATH, FIELD_PASSWORD).send_keys(password)
        driver.find_element(By.XPATH, BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, BUTTON_PROFILE)))

        # Нажать кнопку «Выйти».
        driver.find_element(By.XPATH, BUTTON_PROFILE).click()
        driver.find_element(By.XPATH, BUTTON_LOGOUT).click()

        # Проверить: профиль скрыт, а кнопка «Вход и регистрация» снова отображается.
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, BUTTON_LOGIN_REGISTRATION))
        )
        assert len(driver.find_elements(By.XPATH, BUTTON_PROFILE)) == 0
        assert len(driver.find_elements(By.XPATH, USERNAME)) == 0
        assert driver.find_element(By.XPATH, BUTTON_LOGIN_REGISTRATION).is_displayed() is True
