# Регистрация пользователя
BUTTON_LOGIN_REGISTRATION = "//button[contains(text(), 'Вход и регистрация')]"
BUTTON_NO_ACCOUNT = "//button[contains(text(), 'Нет аккаунта')]"
BUTTON_CREATE_ACCOUNT = "//button[@type='submit' and contains(text(), 'Создать аккаунт')]"
BUTTON_LOGIN = "//button[@type='submit' and contains(text(), 'Войти')]"
BUTTON_LOGOUT = "//button[contains(text(), 'Выйти')]"
BUTTON_PROFILE = "//button[contains(@class, 'circleSmall')]"
FIELD_EMAIL = "//input[@name='email']"
FIELD_PASSWORD = "//input[@name='password']"
FIELD_REPEAT_PASSWORD = "//input[@name='submitPassword']"
USERNAME = "//h3[contains(@class, 'profileText')]"

# Валидация email в форме регистрации
FIELD_ERROR_EMAIL = "//input[@name='email']/parent::div[contains(@class,'input_inputError')]"
FIELD_ERROR_PASSWORD = "//input[@name='password']/parent::div[contains(@class,'input_inputError')]"
FIELD_ERROR_REPEAT_PASSWORD = "//input[@name='submitPassword']/parent::div[contains(@class,'input_inputError')]"
TEXT_ERROR = "//span[contains(text(),'Ошибка')]"
