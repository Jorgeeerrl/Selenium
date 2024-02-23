############################## ELEMENTOS WEB - COMBOBOX ############################
# Para menús desplegables. Tienen una id y dentro cada opción tiene un value y un texto.
# Podemos o hacer que haga click en el desplegable y luego en la opción deseada o podemos utilizar "select".
# Para ello hay que importar el paquete support.ui que tiene muchas opciones para seleccionar este tipo de elementos.

from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


@mark.ui
def test_combobox():
    driver=webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    select_file = Select(driver.find_element(By.ID, 'country')) # Esto selecciona el elemento.
    select_file.select_by_value('germany')  # Esto selecciona la opción de ese value directamente.
    time.sleep(2)

# También podemos hacerlo por texto visible. No es el caso pq aquí no tiene, pero normalmente suele
# ser un atributo al inspeccionar. Sería así:

#   select_file.select_by_visible_text('el texto que ponga en el atributo')

