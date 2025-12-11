#  Entrega Final Automation Testing - Germán Rodríguez
## COMPLETADO FINAL
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
   cd proyecto-final-automation-testing-German-Rodriguez
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

---

##  Ejecución de Tests

### Ejecución Local
```bash
# Ejecutar todos los tests
python run_tests.py

# Ejecutar tests específicos
pytest tests/test_login.py -v

# Con reporte HTML
pytest tests/ --html=reporte.html --self-contained-html -v
```

### GitHub Actions (CI/CD)
Los tests se ejecutan automáticamente en cada push o pull request gracias a GitHub Actions:

- **Workflow:** `.github/workflows/tests.yml`
- **Entorno:** Ubuntu + Python 3.9 + Chrome headless
- **Activación:** Push/PR a rama `main`
- **Reporte:** Disponible como artifact descargable en la sección "Actions"

**Configuración implementada:**
- Chrome headless para CI (`--headless`, `--no-sandbox`, `--disable-dev-shm-usage`)
- Instalación automática de dependencias
- Generación y subida de reportes HTML
- Ejecución en entorno limpio Ubuntu


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

---

## Conclusión 

Este proyecto demuestra la implementación completa de un framework de automatización con:
- Buenas prácticas de QA Automation
- Separación clara entre lógica de UI y lógica de pruebas (POM)
- Ejecución robusta mediante pytest
- Logs + reportes + screenshots
- Pruebas API y UI combinadas
- **CI/CD con GitHub Actions para ejecución automática**
- **Reportes automáticos y artifacts descargables**