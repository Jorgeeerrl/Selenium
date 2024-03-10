import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import mark


@mark.actual
@pytest.fixture
def browser():
    # Inicializa el navegador
    driver = webdriver.Chrome()
    yield driver
    # Cierra el navegador después de cada prueba
    driver.quit()


def test_check_play_buttons(browser):
    # Abre la página web
    browser.get("https://hackmd.io/@penaltis/penaltis")

    # Encuentra todos los botones con el símbolo de reproducción
    play_buttons = browser.find_elements(By.CLASS_NAME, "emoji")

    # Itera sobre los botones y comprueba los enlaces
    for button in play_buttons:
        # Haz clic en el botón
        button.click()

        # Comprueba si la URL actual contiene "acestream://"
        if "acestream://" in browser.current_url:
            print("True")
            assert True  # Marca la prueba como pasada
        else:
            print("False")
            assert False  # Marca la prueba como fallida

        # Regresa a la página principal
        browser.back()
