from uuid import uuid4

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import (
    BLOCK_MY_ADS,
    BUTTON_CATEGORY_DROPDOWN,
    BUTTON_CITY_DROPDOWN,
    BUTTON_CREATE_AD,
    BUTTON_LOGIN,
    BUTTON_LOGIN_REGISTRATION,
    BUTTON_PROFILE,
    BUTTON_PUBLISH_AD,
    FIELD_AD_DESCRIPTION,
    FIELD_AD_NAME,
    FIELD_AD_PRICE,
    FIELD_EMAIL,
    FIELD_PASSWORD,
    FORM_CREATE_AD,
    OPTION_CATEGORY_BOOKS,
    OPTION_CITY_SPB,
    RADIO_CONDITION_USED_LABEL,
)


def test_create_ad_authorized_user(driver, existing_user_credentials):
    email, password = existing_user_credentials
    ad_title = f"Тестовое объявление {uuid4().hex[:8]}"

    # Авторизоваться под заранее созданным пользователем.
    driver.find_element(By.XPATH, BUTTON_LOGIN_REGISTRATION).click()
    driver.find_element(By.XPATH, FIELD_EMAIL).send_keys(email)
    driver.find_element(By.XPATH, FIELD_PASSWORD).send_keys(password)
    driver.find_element(By.XPATH, BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, BUTTON_PROFILE)))

    # Нажать кнопку «Разместить объявление».
    driver.find_element(By.XPATH, BUTTON_CREATE_AD).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, FIELD_AD_NAME)))
    form = driver.find_element(By.XPATH, FORM_CREATE_AD)

    # Заполнить «Название», «Описание товара», «Стоимость» (числовой формат).
    form.find_element(By.XPATH, FIELD_AD_NAME).send_keys(ad_title)
    form.find_element(By.XPATH, FIELD_AD_DESCRIPTION).send_keys("Описание тестового товара для проверки автотеста.")
    form.find_element(By.XPATH, FIELD_AD_PRICE).send_keys("12345")

    # Выбрать «Категорию» и «Город» из Dropdown.
    form.find_element(By.XPATH, BUTTON_CATEGORY_DROPDOWN).click()
    category_option = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, OPTION_CATEGORY_BOOKS))
    )
    driver.execute_script("arguments[0].click();", category_option)
    form.find_element(By.XPATH, BUTTON_CITY_DROPDOWN).click()
    city_option = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, OPTION_CITY_SPB))
    )
    driver.execute_script("arguments[0].click();", city_option)

    # Выбрать RadioButton «Состояние товара».
    form.find_element(By.XPATH, RADIO_CONDITION_USED_LABEL).click()

    # Нажать кнопку «Опубликовать».
    form.find_element(By.XPATH, BUTTON_PUBLISH_AD).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, BUTTON_PROFILE)))

    # Перейти в профиль пользователя.
    driver.get("https://qa-desk.education-services.ru/profile")

    # Проверить: в блоке «Мои объявления» отображается созданное объявление.
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, BLOCK_MY_ADS)))
    assert WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, f"//*[contains(text(),'{ad_title}')]"))
    )
