import time
from pages.inventory_page import InventoryPage


def test_verificar_catalogo(login_in_driver):
    """Verifica que el catálogo y los elementos principales se muestren correctamente."""

    driver = login_in_driver
    inventory = InventoryPage(driver)

    # Esperar a que carguen los productos
    inventory.wait_for_products()

    # Validar título
    titulo = driver.find_element(*InventoryPage.TITLE).text
    assert titulo == "Products", f"Se esperaba 'Products', pero se encontró '{titulo}'"

    # Verificar que haya productos
    productos = driver.find_elements(*InventoryPage.ITEM_CONTAINER)
    assert len(productos) > 0, "No se encontraron productos visibles."

    # Validar elementos visibles del catálogo
    menu_boton = driver.find_element(*InventoryPage.MENU_BTN)
    filtro = driver.find_element(*InventoryPage.SORT_CONTAINER)

    assert menu_boton.is_displayed(), "El botón del menú no es visible."
    assert filtro.is_displayed(), "El selector de filtro no es visible."

    # Mostrar información del primer producto
    primer_producto = productos[0]
    nombre = primer_producto.find_element(*InventoryPage.PRODUCT_NAME).text
    precio = primer_producto.find_element(*InventoryPage.PRODUCT_PRICE).text
    print(f"Primer producto: {nombre} - Precio: {precio}")
