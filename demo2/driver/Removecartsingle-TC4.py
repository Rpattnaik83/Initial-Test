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
    driver.find_element_by_xpath("//a[@class='btn btn-success']").click() # click on proceed
    time.sleep(2)
    driver.find_element_by_xpath("//li[1]/div[4]/a[1]").click() # click on Remove link for Orange item
    #here need to develop whether oranges is present in page or not. if not present passed. else fail    