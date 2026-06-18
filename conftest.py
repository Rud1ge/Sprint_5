from uuid import uuid4

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.data import EXISTING_USER_EMAIL, TEST_PASSWORD
from tests.locators import (
    BUTTON_CREATE_ACCOUNT,
    BUTTON_LOGIN_REGISTRATION,
    BUTTON_LOGOUT,
    BUTTON_NO_ACCOUNT,
    BUTTON_PROFILE,
    FIELD_EMAIL,
    FIELD_PASSWORD,
    FIELD_REPEAT_PASSWORD,
)
from tests.urls import BASE_URL


@pytest.fixture
def driver():
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def existing_user_credentials(driver):
    email = EXISTING_USER_EMAIL.format(uuid=uuid4())
    password = TEST_PASSWORD
    driver.find_element(By.XPATH, BUTTON_LOGIN_REGISTRATION).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_NO_ACCOUNT))).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, FIELD_EMAIL)))
    driver.find_element(By.XPATH, FIELD_EMAIL).send_keys(email)
    driver.find_element(By.XPATH, FIELD_PASSWORD).send_keys(password)
    driver.find_element(By.XPATH, FIELD_REPEAT_PASSWORD).send_keys(password)
    driver.find_element(By.XPATH, BUTTON_CREATE_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_contains("regiatration"))
    driver.get(BASE_URL)
    if driver.find_elements(By.XPATH, BUTTON_PROFILE):
        driver.find_element(By.XPATH, BUTTON_PROFILE).click()
        driver.find_element(By.XPATH, BUTTON_LOGOUT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, BUTTON_LOGIN_REGISTRATION))
        )
    return email, password
