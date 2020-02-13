'''
Created on 26-Jan-2020

@author: skjag
'''
import time
from selenium import webdriver

dynamicBrowsers = "Chrome"
webdriver.driver= None
if dynamicBrowsers == "Chrome":
    driver = webdriver.Chrome('C:\\Users\\skjag\\drivers\\chromedriver')  # Optional argument, if not specified will search path.
    driver.maximize_window()
    driver.get("https://www.facebook.com");
    #time.sleep(10) #this is dynamic wait which will cause program to wait min 10 secs to move forward
    driver.implicitly_wait(10) # here prog will not wait till 10 secs over . the moment elements will be found prog will move on. and it is applicable to all findelement 
    driver.find_element_by_id("email").send_keys("rulapattnaik@gmail.com")
    driver.find_element_by_name("pass").send_keys("rula1982")
    #driver.find_element_by_id("u_0_b").click()
    driver.find_element_by_xpath("//*[@id='u_0_2']").click()
    
''' another peice of code for get_attribute
a=driver.find_element_by_id("email")
a.send_keys("rulapattnaik@gmail.com")
b=a.get_attribute(value)
c=driver.find_element_by_name("Remember")
d=c.getAttribute("Checked")
'''