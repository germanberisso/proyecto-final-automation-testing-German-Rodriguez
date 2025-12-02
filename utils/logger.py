import logging
import os


def get_logger():
    logger = logging.getLogger("automation")

    # Si ya tiene handlers, lo devuelve directamente (para evitar duplicados)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    # Crear carpeta reports si no existe
    os.makedirs("reports", exist_ok=True)

    # Crear archivo de log
    fh = logging.FileHandler("reports/logs.log")
    fh.setLevel(logging.INFO)

    # Formato del log
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    # Log también en consola
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger