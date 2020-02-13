'''
Created on 28-Jan-2020

@author: skjag
'''
import time
from selenium import webdriver
import pytest
#@pytest.mark.skip("Don't execute this test case")-- this the decorator used to skip the testcase from execution 
#If from command prompt we want to execute perticular test case 
@pytest.mark.skip
def test_driverconnection():
    dynamicBrowsers = "Chrome"
    webdriver.driver= None
    if dynamicBrowsers == "Chrome":
        driver = webdriver.Chrome('C:\\Users\\skjag\\drivers\\chromedriver.exe')  # Optional argument, if not specified will search path.
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://54.165.187.107/');
@pytest.mark.skip     
def test_addapplecart():
    Browsers = "Chrome"
    webdriver.driver= None
    if Browsers == "Chrome":
        driver = webdriver.Chrome('C:\\Users\\skjag\\drivers\\chromedriver')  # Optional argument, if not specified will search path.
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://54.165.187.107/');
    if  driver.title== "NodeJS Shopping Cart":
        print("welcome to home page and scenario1 is passed")
        driver.find_element_by_xpath('//html/body/div[2]/div/div/div/div/a').click() #click Add to cart link in apple div
        time.sleep(2)
        driver.find_element_by_xpath("//a[@class='dropdown-toggle']").click() #using chropath, click on cart
        time.sleep(5)
        print("Apple added succefuly and please click on proceed")
        driver.find_element_by_xpath("//a[@class='btn btn-success']").click() #click on Proceed Button
#         a = driver.find_element_by_xpath("//strong[contains(text(),'Apples')]").text # get header apple name
#         print(a)
#         b=driver.find_element_by_xpath("//div[@class='col-xs-2 text-right']//span[@class='badge'][contains(text(),'1')]").text #get quantity number 
#         print(b)
#         c=driver.find_element_by_xpath("//div[@class='col-xs-3 text-right']").text
#         print(c)
#         if a=="Apple" and b=="1" and c=="25 CHF":
#             print("Add cart is successful for Apple and Scenario 2 is passed")
