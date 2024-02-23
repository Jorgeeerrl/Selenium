########################################## NAVEGADOR - COOKIES  ########################################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pytest import mark


@mark.ui
def test_navegacion_cookies():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    print("COOKIES: ", driver.get_cookies())  # Invoca el método get.cookies del driver
                                              # Devuelve las cookies que tiene el driver en ese momento.
    
    driver.add_cookie({"name":"udemy","value":"cookies browser"}) # Dándole un nombre y un valor agrega una cookie.
    print("COOKIES: ", driver.get_cookies())

# En consola aparece la nueva cookie con sus atributos: COOKIES:  [{'domain': 'testautomationpractice.blogspot.com',
    # 'httpOnly': False, 'name': 'udemy', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'cookies browser'}]

    driver.delete_cookie("udemy") # Borra la cookie que hemos creado. Se usa el name.
    print("COOKIES: ", driver.get_cookies())
    
    driver.add_cookie({"name":"udemy","value":"cookies browser"})
    print("COOKIES: ", driver.get_cookies())
    
    driver.delete_all_cookies() # Borra todas las cookies.
    print("COOKIES: ", driver.get_cookies())

    time.sleep(2)

# Este es un método standar para eliminar el banner de cookies:

    driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(2)

    try:
        driver.find_element(By.ID, "cookieChoiceDismiss").click()
    except:
        pass

    time.sleep(2)
