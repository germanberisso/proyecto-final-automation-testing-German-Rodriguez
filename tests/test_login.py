import pytest
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
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


def test_login_incorrecto(driver):
    """Verifica que credenciales incorrectas muestren mensaje de error usando datos aleatorios."""
    
    fake = Faker()
    login_page = LoginPage(driver)
    login_page.open()
    
    # Generar credenciales aleatorias
    usuario_falso = fake.user_name()
    password_falsa = fake.password()
    
    # Intentar login con credenciales incorrectas
    login_page.login(usuario_falso, password_falsa)
    
    # Validar mensaje de error
    error_message = login_page.get_error_message()
    assert error_message is not None, "No se mostró mensaje de error"
    assert "Username and password do not match" in error_message, f"Mensaje inesperado: {error_message}"