from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import BUTTON_CREATE_AD, MODAL_AUTH_REQUIRED_TITLE


class TestCreateAdUnauthorizedUser:
    def test_create_ad_unauthorized_user(self, driver):
        # Нажать кнопку «Разместить объявление».
        driver.find_element(By.XPATH, BUTTON_CREATE_AD).click()

        # Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь».
        modal_title = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, MODAL_AUTH_REQUIRED_TITLE))
        )
        assert modal_title.text == "Чтобы разместить объявление, авторизуйтесь"
