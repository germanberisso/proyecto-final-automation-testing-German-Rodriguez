#  Entrega Final Automation Testing - Germán Rodríguez

##  Propósito del proyecto
Este proyecto forma parte de la **entrega final del curso de Automatización con Python y Selenium**.  
Su objetivo es automatizar flujos básicos de navegación en el sitio [saucedemo.com](https://www.saucedemo.com), validando el login, la navegación por el catálogo y la interacción con el carrito de compras.

El trabajo demuestra el uso de **Selenium WebDriver**, **Pytest** y **esperas explícitas**, así como la correcta estructura del proyecto y generación de reportes automáticos.

---

##  Tecnologías utilizadas
-  Python  
-  Selenium WebDriver  
-  Pytest  
-  Git y GitHub (control de versiones)
-  Pytest-HTML (para reportes de ejecución)
-  POM(Page Object Model)

---

##  Instalación de dependencias

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/germanberisso/proyecto-final-automation-testing-German-Rodriguez


## Estructura del proyecto
proyecto-final-automation-testing-German-Rodriguez/
│
├── tests/                  
│   ├── test_carrito.py
│   ├── test_catalogo.py
│   ├── test_login.py
│   └── api/
│       └── test_api_reqres.py
│
├── pages/                  
│   ├── login_page.py
│   ├── catalog_page.py
│   └── carrito_page.py
│
├── utils/                  
│
├── reports/                
│
├── requirements.txt        
└── README.md

## Conclusion 

Este proyecto demuestra la implementación completa de un framework de automatización con:
Buenas prácticas de QA Automation
Separación clara entre lógica de UI y lógica de pruebas (POM)
Ejecución robusta mediante pytest
Logs + reportes + screenshots
Pruebas API y UI combinadas.