########################################## NAVEGADOR - WINDOWS ########################################

# Cuando pinchamos en hipervínculos que nos llevan a otras páginas.
# IMPORTANTE - window_handles no hace distinción entre ventanas y pestañas. Hay que tenerlo en cuenta 
# cuando introduzcamos el índice en los switch_to.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pytest import mark


@mark.ui
def test_navegacion_windows():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    print(driver.current_window_handle) # Esto devuelve el objeto actual de la ventana abierta.
    print(len(driver.window_handles)) # Devuelve la longitud de la lista de windows handles, que es una lista
                                      # de todas las pestañas y ventanas del navegador que tenemos abiertas.

    driver.find_element(By.CLASS_NAME, "feed-link").click()
    print(len(driver.window_handles)) # Nótese el plural de handleS.
    time.sleep(2)

    driver.switch_to.new_window("tab")  # Crea una nueva pestaña.
    print(len(driver.window_handles)) 
    time.sleep(2)

    driver.close()  # Cierra la pestaña actual.
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[0])  # Vuelve a la pestaña del índice 1.
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])  # Vuelve a la pestaña del índice 1.
    time.sleep(2)

    driver.set_window_size(1028, 768)  # Cambia la resolución de la ventana.
    time.sleep(2)

    driver.switch_to.new_window("window")  # Crea una nueva ventana (que será window_handles[3]).
    time.sleep(2)

    driver.maximize_window()  # Maximiza la ventana.
    time.sleep(2)

    driver.minimize_window()  # Minimiza la ventana.
    time.sleep(2)


    
