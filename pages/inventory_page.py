from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    # Selectores principales
    ITEM_CONTAINER = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".inventory_item button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    # Selectores usados por test_verificar_catalogo
    TITLE = (By.CLASS_NAME, "title")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    SORT_CONTAINER = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_products(self):
        """Espera a que cargue la lista de productos."""
        self.wait.until(EC.presence_of_all_elements_located(self.ITEM_CONTAINER))

    def get_products(self):
        """Retorna la lista de productos visibles en pantalla."""
        self.wait_for_products()
        return self.driver.find_elements(*self.ITEM_CONTAINER)

    def add_first_product(self):
        """Hace clic en el botón Add to Cart del primer producto."""
        self.wait_for_products()
        first_button = self.driver.find_element(*self.ADD_TO_CART_BTN)
        first_button.click()

    def add_product_by_name(self, name):
        """Agrega un producto al carrito buscando por su nombre."""
        self.wait_for_products()
        products = self.get_products()

        for product in products:
            title = product.find_element(*self.PRODUCT_NAME).text
            if title.lower() == name.lower():
                product.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
                return

        raise Exception(f"No se encontró el producto con nombre: {name}")

    def get_cart_count(self):
        """Retorna cuántos productos muestra el ícono del carrito."""
        badge = self.wait.until(EC.presence_of_element_located(self.CART_BADGE))
        return badge.text

    def go_to_cart(self):
        """Navega al carrito y espera a que cargue."""
        self.driver.find_element(*self.CART_LINK).click()
        self.wait.until(EC.url_contains("/cart.html"))