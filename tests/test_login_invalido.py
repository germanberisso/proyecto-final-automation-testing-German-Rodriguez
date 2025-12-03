import pytest
import time
from pages.login_page import LoginPage


def test_login_invalido(driver):
    """Verifica que el sistema muestre un mensaje de error cuando las credenciales son inválidas."""

    login_page = LoginPage(driver)
    login_page.open()

    # Usamos credenciales incorrectas
    login_page.login("standard_user", "password_incorrecta")

    # Obtener mensaje de error desde el Page Object
    error_text = login_page.get_error_message()

    # Validar mensaje esperado
    assert error_text is not None, "No apareció mensaje de error."
    assert "Epic sadface" in error_text, f"Mensaje inesperado: {error_text}"
