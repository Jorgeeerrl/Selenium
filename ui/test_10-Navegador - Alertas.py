########################################## NAVEGADOR - ALERTAS ########################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
from pytest import mark


@mark.ui
def test_navegacion_alertas():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    try:
        driver.find_element(By.ID, "cookieChoiceDismiss").click()
    except:
        pass

    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button[1]').click()
    time.sleep(2)

    alert = Alert(driver)
    texto = alert.text
    print("Texto Alerta: ", texto)

    alert.accept() # La acepta. "alert.dismiss()" la rechazaría.
    print("Texto Alerta: ", texto)

#   assert driver.find_element(By.ID, "demo").text == "You pressed OK!" # Valida según lo esperado.
    time.sleep(2)