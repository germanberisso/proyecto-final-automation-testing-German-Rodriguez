# pages/CartPage.py

from selenium.webdriver.common.by import By

class CartPage:

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def get_products(self):
        """Devuelve la lista de productos en el carrito."""
        return self.driver.find_elements(*self.CART_ITEMS)

    def get_first_product_name(self):
        """Devuelve el nombre del primer producto del carrito."""
        products = self.get_products()

        if not products:
            raise Exception("No hay productos en el carrito.")

        return products[0].find_element(*self.PRODUCT_NAME).text

    def get_all_product_names(self):
        """Devuelve una lista con los nombres de TODOS los productos del carrito."""
        products = self.get_products()
        return [
            p.find_element(*self.PRODUCT_NAME).text
            for p in products
        ]

