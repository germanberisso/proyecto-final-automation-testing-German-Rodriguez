# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.screenshot import take_screenshot
from utils.logger import get_logger
from utils.helpers import login

logger = get_logger()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Tipo de navegador: chrome o edge"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "edge":
        from selenium.webdriver.edge.service import Service as EdgeService
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)

    driver.maximize_window()
    logger.info(f"Navegador iniciado: {browser}")

    yield driver

    try:
        driver.quit()
        logger.info("Navegador cerrado")
    except Exception as e:
        # Evitar que teardown falle y dispare screenshot
        logger.warning(f"Error al cerrar navegador: {e}")
        pass


@pytest.fixture
def login_in_driver(driver):
    """Realiza login antes de cada test que lo requiera."""
    logger.info("Ejecutando login previo al test...")
    login(driver)
    return driver


# CAPTURA DE PANTALLA EN CASO DE ERROR
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    # Solo capturar screenshot si el test FALLA durante la fase de "call"
    if report.failed and report.when == "call":
        driver = item.funcargs.get("driver", None)
        if driver:
            test_name = item.name
            logger.error(f"Test fallado: {test_name}. Capturando screenshot...")
            take_screenshot(driver, test_name)