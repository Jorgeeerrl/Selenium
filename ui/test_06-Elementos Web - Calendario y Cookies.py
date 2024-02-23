############################ ELEMENTOS WEB - CALENDARIO ###########################


from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@mark.ui
def test_calendario():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")

    # Cerrar el banner de cookies si está presente
    try:
        driver.find_element(By.ID, "cookieChoiceDismiss").click()
    except:
        pass

    calendario = driver.find_element(By.XPATH, '//*[@id="datepicker"]')
    driver.execute_script("arguments[0].scrollIntoView();", calendario)
    calendario.click()

    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@class = "ui-state-default" and text() = "14"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="datepicker"]').click()
    driver.find_element(By.XPATH, '//*[@class = "ui-state-default" and text() = "23"]').click()
    time.sleep(2)

# Para que imprima en consola el contenido y comprobar con pytest -s si lo hace correctamente:

    calendario_content = calendario.get_attribute("value")  # Si es un input tipo texto
    print("Contenido del elemento calendario:", calendario_content)

# Y para limpiar el contenido y añadir una fecha modo texto:

    calendario.clear()
    calendario.send_keys('17/03/1985')
    time.sleep(2)

    calendario_content = calendario.get_attribute("value")
    print("Contenido del elemento calendario:", calendario_content)