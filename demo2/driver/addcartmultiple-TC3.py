'''
Created on 27-Jan-2020

@author: skjag
'''
import time
from selenium import webdriver
dynamicBrowsers = "Chrome"
webdriver.driver= None
if dynamicBrowsers == "Chrome":
    driver = webdriver.Chrome('C:\\Users\\skjag\\drivers\\chromedriver')  # Optional argument, if not specified will search path.
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://54.165.187.107/');
driver.find_element_by_xpath("//div[3]//a[1]").click() #click Add to cart link in orange div
time.sleep(2)
driver.find_element_by_xpath("//div[4]//a[1]").click() #click Add to cart link in garlic div    
time.sleep(2)
driver.find_element_by_xpath("//a[@class='dropdown-toggle']").click() #using chropath, click on cart
time.sleep(5)
print("Orange and Garlic  added succefuly and please click on proceed")
driver.find_element_by_xpath("//a[@class='btn btn-success']").click()
print("Now we are in Cart page for orange and garlic validation")
orng_qty=driver.find_element_by_xpath("//div[@class='col-xs-2 text-right']//span[@class='badge'][contains(text(),'1')]").text #get orange quantity number 
orng_price=driver.find_element_by_xpath("//div[@class='col-xs-3 text-right']").text #get orange price
garlic_qty=driver.find_element_by_xpath("//div[@class='col-xs-2 text-right']//span[@class='badge'][contains(text(),'1')] ").text #get orange quantity number 
garlic_price=driver.find_element_by_xpath("//li[2]//div[3]").text #get orange price


if driver.find_element_by_xpath("//strong[contains(text(),'Oranges')]") and driver.find_element_by_xpath("//strong[contains(text(),'Garlic')]") and orng_qty=="1" and orng_price=="30 CHF" and garlic_qty=="1" and garlic_price =="15 CHF" :
    print("Add cart is successful for orange and Garlic")

