################################ TEXTBOX - IFRAME ################################

# Muchas veces encontramos que una etiqueta (o cualquier elemento HTML) no es visible pq está en un iframe.
# Un iframe es un contenedor de frames y Selenium nos permite buscar un elemento web dentro de ellos.


from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@mark.ui
def test_element_textbox_iframe():
    driver = webdriver.Chrome()  
    driver.get("https://testautomationpractice.blogspot.com/")



    textbox = driver.find_element(By.ID, "RESULT_TextField-0")  # Selecciona el elemento.
    textbox.send_keys("Jorge")
    time.sleep(2)
    textbox.clear()  # Borra su contenido
    textbox.send_keys("Roncal")
    time.sleep(2)
    actual_value = textbox.get_attribute('value')  # Obtiene el atributo value y lo almacena en una variable.
    print(actual_value)  # Imprimimos la variable para comprobarlo.