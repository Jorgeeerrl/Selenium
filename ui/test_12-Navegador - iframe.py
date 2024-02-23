########################################## NAVEGADOR - IFRAME  ########################################

# Para trabajar con elementos que están dentro de un iframe y al referenciarlos en el código a través de sus atributos 
# nos dice que no está el elemento. Este error es porque se encuentra dentro de un iframe y no se puede acceder a él
# directamente.
# Cambiamos primero al iframe y luego ya accedemos al elemento deseado.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pytest import mark


@mark.ui
def test_navegacion_iframe():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    driver.switch_to.frame("frame-one796456169")

    driver.find_element(By.ID, "RESULT_TextField-0").send_keys("Jorge")
    time.sleep(2)