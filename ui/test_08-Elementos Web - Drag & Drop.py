############################## ELEMENTOS WEB - DRAG & DROP ############################

from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


@mark.ui
def test_drag_and_drop():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    try:
        driver.find_element(By.ID, "cookieChoiceDismiss").click()
    except:
        pass

    time.sleep(2)

    scroll = driver.find_element(By.XPATH, '//*[@id="draggable"]')
    driver.execute_script("arguments[0].scrollIntoView();", scroll)

    drag = driver.find_element(By.ID, 'draggable')
    drop = driver.find_element(By.ID, 'droppable')

    action = ActionChains(driver)
    
    action.drag_and_drop(drag, drop).perform()
    time.sleep(2)