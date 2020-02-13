'''
Created on 28-Jan-2020

@author: skjag
'''

import time
import pytest
from selenium import webdriver
from selenium.webdriver.remote import webelement
from selenium.webdriver.remote.webelement import WebElement
from driver.driverconnection import driver
from pip._vendor.requests.sessions import session
dynamicBrowsers = "Chrome"
webdriver.driver= None

webpage_name = "NodeJS Shopping Cart"

@pytest.fixture(session)
def test_setup():
    global driver
    if dynamicBrowsers == "Chrome":
        driver = webdriver.Chrome('C:\\Users\\skjag\\drivers\\chromedriver')  # Optional argument, if not specified will search path.
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("TEST COMPLETE")

def test_login(test_setup):
    driver.get('http://54.165.187.107/');
    if driver.title == webpage_name:
        print("Shopping Cart Page accessible")
        print("TC_1: PASS")
    else:
        print("NodeJS Shopping Cart not accessible")
        print("TC_1: FAIL")

    
        
        