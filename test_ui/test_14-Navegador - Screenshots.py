########################################## NAVEGADOR - SCREENSHOTS ########################################

# Para que haga un screenshot de cómo estaba estaba la página antes de dar un fallo.

from selenium import webdriver
import time
from pytest import mark

@mark.ui
def test_navegador_screenshots():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    time.sleep(2)
    driver.save_screenshot("./imagen.png") # donde pone ./ podemos poner su ruta de guardado.
