import pytest
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_login_exitoso(driver):
    """Verifica que un usuario válido pueda iniciar sesión correctamente usando POM."""

    login_page = LoginPage(driver)
    login_page.open()

    # Ejecutar login
    login_page.login("standard_user", "secret_sauce")

    # Validar redirección
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url, "No se redirigió a inventory."

    # Validar título de la página
    titulo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(("class name", "title"))
    ).text
    assert titulo == "Products", f"Se esperaba 'Products', se encontró '{titulo}'"