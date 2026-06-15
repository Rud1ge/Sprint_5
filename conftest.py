import subprocess
import time
from urllib import request
from urllib.error import URLError

import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service


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
    driver.get("https://qa-desk.education-services.ru/")

    yield driver

    driver.quit()
