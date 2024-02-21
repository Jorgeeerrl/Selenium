################################## CLASS NAME #################################
from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@mark.ui
def test_element_by_class_name():
    driver = webdriver.Chrome()  # Crea un driver tipo Chrome
    driver.get('https://automationexercise.com/')

    web_element = driver.find_element(By.CLASS_NAME, 'btn-success')
    web_element.click()
    # Si hay + de 1 elemento con esa clase actúa sobre el primero.

              ### También se podría hacer así ###
    # driver.find_element(By.CLASS_NAME,'btn-success').click()

    time.sleep(5)

# Si tuviéramos varios elemento con la misma clase y queremos uno en concreto:

#ctrl+f  -------> Para ver si hay coincidencias y dónde.
#ctrl+b  ------|

@mark.ui
def test_element_by_class_name_2():
    driver = webdriver.Chrome()  # Crea un driver tipo Chrome
    driver.get('https://automationexercise.com/')

    web_elements = driver.find_elements(By.CLASS_NAME, 'btn-success') # nótese la s de elementS.
    print("Cantidad de elementos Clase: ", len(web_elements)) # Nos diría cuántos hay.
    web_elements[0].click()  # Esto haría la acción en el elemento de ese índice de la lista.
    time.sleep(5)
    web_elements[1].click()
    time.sleep(5)
