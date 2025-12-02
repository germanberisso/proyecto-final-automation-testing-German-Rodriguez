import os
from datetime import datetime

def take_screenshot(driver, test_name):
    """Guarda captura de pantalla en la carpeta reports/screenshots."""
    
    folder = "reports/screenshots"
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"{folder}/{test_name}_{timestamp}.png"

    driver.save_screenshot(file_path)
    return file_path