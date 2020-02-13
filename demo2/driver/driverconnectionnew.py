'''
Created on 26-Jan-2020

@author: skjag
'''
import time
from selenium import webdriver
from selenium.webdriver.remote import webelement
from selenium.webdriver.remote.webelement import WebElement

dynamicBrowsers = "Chrome"
webdriver.driver= None
if dynamicBrowsers == "Chrome":
    driver = webdriver.Chrome('C:\\Users\\skjag\\drivers\\chromedriver')  # Optional argument, if not specified will search path.
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://54.165.187.107/');
if driver.title== "NodeJS Shopping Cart":
    print("welcome to home page and scenario1 is passed")
driver.find_element_by_xpath('//html/body/div[2]/div/div/div/div/a').click() #click Add to cart link in apple div
time.sleep(2)
driver.find_element_by_xpath("//a[@class='dropdown-toggle']").click() #using chropath, click on cart
time.sleep(5)
print("Apple added succefuly and please click on proceed")
driver.find_element_by_xpath("//a[@class='btn btn-success']").click() #click on Proceed Button
a = driver.find_element_by_xpath("//strong[contains(text(),'Apples')]").text # get header apple name
print(type(a))
print(a)
b=driver.find_element_by_xpath("//div[@class='col-xs-2 text-right']//span[@class='badge'][contains(text(),'1')]").text #get quantity number 
print(type(b))
print(b)
c=driver.find_element_by_xpath("//div[@class='col-xs-3 text-right']").text
print(type(c))
print(c)
if a=="Apples" and b=="1" and c=="25 CHF":
    print("Add cart is successful for Apple and Scenario 2 is passed")   

# time.sleep(2)
# driver.find_element_by_xpath("//a[@class='btn btn-default']").click() #click on Remove Button
#/html[1]/body[1]/div[2]/ul[1]/li[1]/div[1]/strong[1]
# /html/body/div[3]/div/div/div/div/a # orange
# /html/body/div[4]/div/div/div/div/a #Garlic
# /html/body/div[5]/div/div/div/div/a #papeya
#print(driver.find_element_by_xpath('//html/body/div[1]/div[2]/div/div').text)#items in cart sqare for proceed
# if driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div').text:
#     print("Test case 1 is passed")
#a = driver.find_element_by_xpath('//html/body/div[1]/div[2]/div/div').text
#print(type(a))
#print(a[0])


# if driver.find_element_by_xpath("//strong[contains(text(),'Apples')]"):
#     print("Add cart is successful for Apple")
