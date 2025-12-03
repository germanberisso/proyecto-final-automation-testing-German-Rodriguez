import time
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_agregar_producto_al_carrito(login_in_driver):
    """Verifica que se pueda agregar un producto al carrito usando Page Object Model."""

    driver = login_in_driver

    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    # Esperar a que carguen los productos
    inventory.wait_for_products()

    # Agregar primer producto
    inventory.add_first_product()

    # Verificar contador del carrito
    cart_count = inventory.get_cart_count()
    assert cart_count == "1", f"Se esperaba '1' en el carrito, se encontró '{cart_count}'"

    # Ir al carrito
    inventory.go_to_cart()

    # Verificar producto en el carrito
    productos = cart.get_products()
    assert len(productos) > 0, "El carrito aparece vacío pero se agregó un producto."

    # Obtener nombre del primer producto
    nombre_producto = cart.get_first_product_name()
    print(f"Producto agregado al carrito: {nombre_producto}")

