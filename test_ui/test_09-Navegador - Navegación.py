############################## NAVEGADOR - NAVEGACIÓN ############################

from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@mark.ui
def test_navegacion_browser():
    driver = webdriver.Chrome()
    driver.get('https://www.ymicamiseta.com/')
    time.sleep(2)

    try:
        driver.find_element(By.ID, "cookieChoiceDismiss").click()
    except:
        pass

    driver.find_element(By.XPATH, '//*[@id="hm_first"]/a').click()
    time.sleep(2)
    print("URL actual: ", driver.current_url)  # utilizo la propiedad url para imprimir la url actual.

    driver.back()
    time.sleep(2)
    print("URL actual: ", driver.current_url) 
    
    driver.forward()
    time.sleep(2)
    print("URL actual: ", driver.current_url) 


    driver.refresh()
    time.sleep(2)
    print("URL actual: ", driver.current_url)  

    driver.close()