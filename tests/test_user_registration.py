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
    FIELD_ERROR_EMAIL,
    FIELD_ERROR_PASSWORD,
    FIELD_ERROR_REPEAT_PASSWORD,
    FIELD_PASSWORD,
    FIELD_REPEAT_PASSWORD,
    TEXT_ERROR,
    USERNAME,
)


class TestUserRegistration:
    def test_user_registration(self, driver):
        # Нажать кнопку «Вход и регистрация».
        driver.find_element(By.XPATH, BUTTON_LOGIN_REGISTRATION).click()
        # Нажать кнопку «Нет аккаунта».
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_NO_ACCOUNT))
        ).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, FIELD_EMAIL)))
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

    def test_user_registration_not_by_mask(self, driver):
        # Нажать кнопку «Вход и регистрация».
        driver.find_element(By.XPATH, BUTTON_LOGIN_REGISTRATION).click()
        # Нажать кнопку «Нет аккаунта».
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_NO_ACCOUNT))
        ).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, FIELD_EMAIL)))
        # Заполнить поле Email формы регистрации и нажать кнопку «Создать аккаунт».
        driver.find_element(By.XPATH, FIELD_EMAIL).send_keys(f"{uuid4()}")
        driver.find_element(By.XPATH, BUTTON_CREATE_ACCOUNT).click()

        # Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, сообщение «Ошибка» отображается.
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, FIELD_ERROR_EMAIL)))
        assert driver.find_element(By.XPATH, FIELD_ERROR_PASSWORD).is_displayed() is True
        assert driver.find_element(By.XPATH, FIELD_ERROR_REPEAT_PASSWORD).is_displayed() is True
        assert driver.find_element(By.XPATH, TEXT_ERROR).text == "Ошибка"

    def test_user_registration_existing_user(self, driver, existing_user_credentials):
        existing_email, existing_password = existing_user_credentials
        # Нажать кнопку «Вход и регистрация».
        driver.find_element(By.XPATH, BUTTON_LOGIN_REGISTRATION).click()
        # Нажать кнопку «Нет аккаунта».
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_NO_ACCOUNT))
        ).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, FIELD_EMAIL)))
        # Заполнить все поля формы регистрации данными существующего пользователя и нажать «Создать аккаунт».
        driver.find_element(By.XPATH, FIELD_EMAIL).send_keys(existing_email)
        driver.find_element(By.XPATH, FIELD_PASSWORD).send_keys(existing_password)
        driver.find_element(By.XPATH, FIELD_REPEAT_PASSWORD).send_keys(existing_password)
        driver.find_element(By.XPATH, BUTTON_CREATE_ACCOUNT).click()

        # Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, сообщение «Ошибка» отображается.
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, FIELD_ERROR_EMAIL)))
        assert driver.find_element(By.XPATH, FIELD_ERROR_PASSWORD).is_displayed() is True
        assert driver.find_element(By.XPATH, FIELD_ERROR_REPEAT_PASSWORD).is_displayed() is True
        assert driver.find_element(By.XPATH, TEXT_ERROR).text == "Ошибка"
