from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configuración de opciones para Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Modo sin interfaz gráfica
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Indica la ruta del ChromeDriver (en GitHub Actions lo instalaremos automáticamente)
service = Service("chromedriver")

driver = webdriver.Chrome(service=service, options=chrome_options)

# URL que queremos scrapear (puedes usar la URL que necesites)
url = "https://www.infojobs.net/ofertas-trabajo?..."
driver.get(url)

time.sleep(3)  # Espera a que la página cargue

# Ejemplo: extraer títulos de ofertas (ajusta las clases según la página)
jobs = driver.find_elements(By.CLASS_NAME, "offer")
for job in jobs:
    title = job.find_element(By.CLASS_NAME, "title").text
    print(f"Oferta: {title}")

driver.quit()
