################################### ELEMENTOS WEB - CHECKBOX #####################################

from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@mark.ui
def test_element_textbox_iframe():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")

    frame_element = driver.find_element(By.ID, "frame-one796456169")
    driver.switch_to.frame(frame_element)

    checkbox = driver.find_element(By.XPATH, '//*[@id="q2"]/table/tbody/tr[1]/td/label')
    checkbox.click()
    time.sleep(2)

# Para rescatar el argumento de un elemento y verlo en consola, por ejemplo para comprobar si el
#   elemento que hemos selecciona es del tipo que queremos ésto:

    print("Tipo de elemento: ", type(checkbox))
    print("Seleccionado: ", checkbox.is_selected())  # Arroja un True/False



# Es posible que el elemento esté más abajo en la web y necesitemos que el testrunner tire hacia abajo
#   y poder ver el elemento. Sale un mensaje de error de: elemento interceptado, no es clickeable en ese punto.


@mark.ui
def test_element_textbox_iframe_2():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")

    frame_element = driver.find_element(By.ID, "frame-one796456169")
    driver.switch_to.frame(frame_element)

    checkbox = driver.find_element(By.XPATH, '//*[@id="q2"]/table/tbody/tr[1]/td/label')
    driver.execute_script("arguments[0].scrollIntoView();", checkbox)
# Esto le dice al driver que ejecute un script de javascript que le dice que scrollee hasta que se vea el
#   elemento [0] del argumento que le indequemos (en este caso checkbox, que a su vez es el xpath del elemento).
    time.sleep(2)
# Podemos decirle al driver también con un script que clickee el 1er argumento checkbox que encuentre:
    driver.execute_script("arguments[0].click();", checkbox)
    time.sleep(2)
# Para rescatar el argumento de un elementoy verlo en consola, por ejemplo para comprobar si el
#   elemento que hemos selecciona es del tipo que queremos ésto:
    print("Tipo de elemento: ", type(checkbox))
    print("Seleccionado: ", checkbox.is_selected())  # Arroja un True/False

##### Con pytest -m <etiqueta> -s  se reflejan las salidas a consola en el resultado de los test. ###