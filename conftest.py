import subprocess
import time
from urllib import request
from urllib.error import URLError
from uuid import uuid4

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import (
    BUTTON_CREATE_ACCOUNT,
    BUTTON_LOGIN_REGISTRATION,
    BUTTON_NO_ACCOUNT,
    FIELD_EMAIL,
    FIELD_PASSWORD,
    FIELD_REPEAT_PASSWORD,
)


def _send_remote_shutdown_command(self):
    # Selenium #13850: on Windows, urlopen("/shutdown") blocks without timeout.
    try:
        request.urlopen(f"{self.service_url}/shutdown", timeout=1)
    except (URLError, TimeoutError):
        return
    for _ in range(30):
        if not self.is_connectable():
            break
        time.sleep(1)


Service.send_remote_shutdown_command = _send_remote_shutdown_command


@pytest.fixture
def driver():
    service = webdriver.ChromeService(log_output=subprocess.DEVNULL)
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("https://qa-desk.education-services.ru/")
        yield driver
    finally:
        driver.quit()


@pytest.fixture
def existing_user_credentials():
    email = f"existing_user_{uuid4()}@ya.ru"
    password = "Qwerty123!"
    setup_driver = webdriver.Chrome(service=webdriver.ChromeService(log_output=subprocess.DEVNULL))
    try:
        setup_driver.get("https://qa-desk.education-services.ru/")
        setup_driver.find_element(By.XPATH, BUTTON_LOGIN_REGISTRATION).click()
        setup_driver.find_element(By.XPATH, BUTTON_NO_ACCOUNT).click()
        setup_driver.find_element(By.XPATH, FIELD_EMAIL).send_keys(email)
        setup_driver.find_element(By.XPATH, FIELD_PASSWORD).send_keys(password)
        setup_driver.find_element(By.XPATH, FIELD_REPEAT_PASSWORD).send_keys(password)
        setup_driver.find_element(By.XPATH, BUTTON_CREATE_ACCOUNT).click()
        WebDriverWait(setup_driver, 3).until(expected_conditions.url_contains("regiatration"))
    finally:
        setup_driver.quit()

    return email, password
