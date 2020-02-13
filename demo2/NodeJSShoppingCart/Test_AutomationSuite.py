'''
Created on 28-Jan-2020

@author: skjag
'''
import time
from selenium import webdriver
import pytest
import allure
#@pytest.mark.skip("Don't execute this test case")-- this the decorator used to skip the testcase from execution 
#If from command prompt we want to execute perticular test case 
def test_driverconnection_1():
    dynamicBrowsers = "Chrome"
    webdriver.driver= None
    if dynamicBrowsers == "Chrome":
        driver = webdriver.Chrome('C:\\Users\\skjag\\drivers\\chromedriver.exe')  # Optional argument, if not specified will search path.
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://54.165.187.107/');

def test_add_apple_2():
    Browsers = "Chrome"
    webdriver.driver= None
    if Browsers == "Chrome":
        driver = webdriver.Chrome('C:\\Users\\skjag\\drivers\\chromedriver')  # Optional argument, if not specified will search path.
        driver.implicitly_wait(5)
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
        a = driver.find_element_by_xpath("//strong[contains(text(),'Apples')]").text # get header apple name
        b=driver.find_element_by_xpath("//div[@class='col-xs-2 text-right']//span[@class='badge'][contains(text(),'1')]").text #get quantity number 
        c=driver.find_element_by_xpath("//div[@class='col-xs-3 text-right']").text
        assert a=="Apples" and b=="1" and c=="25 CHF"

def test_add_multiple_items3():
    dynamicBrowsers = "Chrome"
    webdriver.driver= None
    if dynamicBrowsers == "Chrome":
        driver = webdriver.Chrome('C:\\Users\\skjag\\drivers\\chromedriver')  # Optional argument, if not specified will search path.
        driver.implicitly_wait(5)
        driver.get('http://54.165.187.107/');
        driver.maximize_window()
    driver.find_element_by_xpath("//div[3]//a[1]").click() # Add to cart link in orange div
    time.sleep(2)
    driver.find_element_by_xpath("//div[4]//a[1]").click() #click Add to cart link in garlic div    
    time.sleep(2)
    driver.find_element_by_xpath("//a[@class='dropdown-toggle']").click() #using chropath, click on cart
    time.sleep(5)
    print("Orange and Garlic added")
    driver.find_element_by_xpath("//a[@class='btn btn-success']").click() # click on proceed
    time.sleep(2)
    print("Now we are in Cart page for orange and garlic validation")
    orng_qty=driver.find_element_by_xpath("//div[@class='col-xs-2 text-right']//span[@class='badge'][contains(text(),'1')]").text #get orange quantity number 
    orng_price=driver.find_element_by_xpath("//div[@class='col-xs-3 text-right']").text #get orange price
    garlic_qty=driver.find_element_by_xpath("//div[@class='col-xs-2 text-right']//span[@class='badge'][contains(text(),'1')] ").text #get orange quantity number 
    garlic_price=driver.find_element_by_xpath("//li[2]//div[3]").text #get orange price
    
    assert orng_qty == "2" and orng_price == "30 CHF" and garlic_qty == "1" and garlic_price == "15 CHF"
    
    
#@pytest.mark.swagat
def test_remove_single_item_4():
    a = 5
    dynamicBrowsers = "Chrome"
    webdriver.driver= None
    if dynamicBrowsers == "Chrome":
        driver = webdriver.Chrome('C:\\Users\\skjag\\drivers\\chromedriver')  # Optional argument, if not specified will search path.
        driver.implicitly_wait(10)
        driver.get('http://54.165.187.107/');
        driver.maximize_window()
        driver.find_element_by_xpath("//div[3]//a[1]").click() #click Add to cart link in orange div
        time.sleep(2)
        driver.find_element_by_xpath("//div[4]//a[1]").click() #click Add to cart link in garlic div    
        time.sleep(2)
        driver.find_element_by_xpath("//a[@class='dropdown-toggle']").click() #click on cart
        time.sleep(5)
        driver.find_element_by_xpath("//a[@class='btn btn-success']").click() # click on proceed
        time.sleep(2)
        driver.find_element_by_xpath("//li[1]/div[4]/a[1]").click() # click on Remove link for Orange item
        time.sleep(2)
        abc = driver.page_source #get the page source
        if 'Oranges' in abc: # search the entire page and look for Oranges
            a = 1
            print('Found')
        else:
            print('not Found')   
            a = 0
        total_val = driver.find_element_by_xpath("//strong[contains(text(),'Total: 15 CHF')]").text #total value should be 15 
        
        assert a == 0 and total_val == "Total: 15 CHF" #check if Oranges are found or not. If not found a should be 0, and Total value should be 15 CHF
    
    
