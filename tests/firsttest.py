import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


def test_add_one_item_to_cart():
    ROOT_DIR = os.path.abspath(os.curdir)
    driver = webdriver.Chrome(ROOT_DIR + '\drivers\chromedriver.exe')
    driver.maximize_window()
    # URL should be come from test data or config file.
    driver.get('https://insomniacookies.com/order')
    search_box = driver.find_element_by_id("addresstext")
    WebDriverWait(driver, 60).until(cond.visibility_of(search_box))
    search_box.send_keys('1084 East Lancaster Ave Byrn Mawr, PA')
    time.sleep(10)
    search_box.send_keys(Keys.DOWN)
    search_box.send_keys(Keys.ENTER)
    locator = '//h5[text()="Bryn Mawr, PA"]/..//button[text()="Delivery"]'
    # delivery = driver.find_element_by_xpath(locator)
    # WebDriverWait(driver, 60).until(cond.visibility_of(delivery))
    # delivery.click()
    # get element  after explicitly waiting for 10 seconds
    delivery = WebDriverWait(driver, 60).until(
        cond.element_to_be_clickable((By.XPATH, "//h5[text()='Bryn Mawr, PA']/..//button[text()='Delivery']/.."))
    )
    # click the element
    delivery.click()
    continueBtn = WebDriverWait(driver, 60).until(
        cond.element_to_be_clickable((By.ID, "address-confirmation-modal-continue-btn"))
    )
    continueBtn.click()
    continueButton = WebDriverWait(driver, 60).until(
        cond.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary btn-block btn-lg mt-0 mt-sm-4 btn-datetime-submit ae-button']"))
    )
    continueButton.click()
    driver.close()
