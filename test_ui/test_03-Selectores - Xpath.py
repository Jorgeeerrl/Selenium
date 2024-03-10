############################## SELECTORES XPATH #################################

# Busca una ruta/ubicación dentro de una jerarquía html de un elemento concreto.

from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import mark
import time

@mark.ui
def test_element_by_xpath_full():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")

    # Botón derecho en el elemento en el html > copiar > Xpath
    # Está el Xpath Full, el cual no es una buena práctica porque si luego se mueve el elemento ocasionará fail:

    web_element = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div["
                                                "4]/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/textarea")
    web_element.send_keys("Jorge")

#    time.sleep(4)


# Y el Xpath normal:

@mark.ui
def test_element_by_xpath():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    web_element = driver.find_element(By.XPATH, '//*[@id="email"]') # Se ponen comillas simples para que no interfieran con las del interior.
    web_element.send_keys("jorgeeerrl")

    time.sleep(4)

# Podemos crear un Xpath nosotros.
# // le dice que empiece desde el principio dew la página.
# * le dice que cualquier elemento.
# [] crea atributos y otra forma de localizar el elemento.
# contains(@class, 'lo_que_sea_aunque_sea_una_parte') le dice que contenga la clase loquesea. Se pueden encadenar.

@mark.ui
def test_element_by_xpath_created():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    web_element = driver.find_element(By.XPATH, '//*[contains(@type, "text") and @id = "field2"]')
    web_element.send_keys("jorgeeerrl")

# Esto viene muy bien para cuando hay varios elementos que comparten un atributo y queremos diferenciarlos.

    time.sleep(4)