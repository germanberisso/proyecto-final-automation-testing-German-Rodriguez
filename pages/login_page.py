# pages/login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON   = (By.ID, "login-button")
    ERROR_MESSAGE  = (By.CSS_SELECTOR, "h3[data-test='error']")

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Abre la página de login."""
        self.driver.get(self.URL)
        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))

    def login(self, username, password):
        """Completa usuario y contraseña y hace clic en Login."""
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        """Devuelve el mensaje de error si aparece, sino None."""
        try:
            error = self.wait.until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return error.text
        except:
            return None