from selenium import webdriver  # Importa el paquete webdriver de Selenium.
from selenium.webdriver.common.by import By  # Importa el módulo By de webdriver.
import time

def test_element_by_class():
    driver = webdriver.Chrome()  # Crea un webdriver de Chrome.
    driver.get('https://www.domestika.org/es/ymicamiseta')  # Carga la página web.

    web_element = driver.find_element(By.CLASS_NAME, 'a-placeholder')  # Encuentra el elemento web de la clase 'a-placeholder'
                                                                      #   y lo almacena en la variable web_element.
    web_element.click()  # Hace una acción (click) sobre el elemento web almacenado en la variable.
    time.sleep(10)

    driver.find_element(By.CLASS_NAME, 'js-amplitude-track').click()  # Así lo hace de una.

    time.sleep(10)
