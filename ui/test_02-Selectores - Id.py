################################# SELECTORES - ID / NAME ####################################

from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@mark.ui
def test_element_by_name():
    driver = webdriver.Chrome()  # Crea un driver tipo Chrome
    driver.get('https://automationexercise.com/contact_us')

    driver.find_element(By.NAME, 'email').send_keys("Jorge")

    time.sleep(5)

### También se podría hacer así ###

#    web_element = driver.find_element(By.NAME, 'email')
#    web_element.send_keys("Jorge")

#    time.sleep(5)

@mark.ui
def test_element_by_id():
    driver = webdriver.Chrome()  # Crea un driver tipo Chrome
    driver.get('https://automationexercise.com/contact_us')

    driver.find_element(By.ID, 'message').send_keys("Jorge")

    time.sleep(5)
#ctrl+f  -------> Para ver si hay coincidencias y dónde.
#ctrl+b  ------|