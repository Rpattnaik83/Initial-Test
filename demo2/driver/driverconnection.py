'''
Created on 25-Jan-2020

@author: skjag
'''

print('helloworld')

import selenium

##print(selenium.__version__)
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

# class RunChrome():
#     def test(self):
# #       driverlocation = "C:\\Users\\skjag\\drivers\\chromedriver"
# #       os.environ["webdriver.chrome.driver"]=driverlocation
#         driver = webdriver.Chrome()
#         #driver = webdriver.Chrome(executable_path='C:\Users\skjag\drivers\chromedriver.exe')
#        
#         #driver.get("http://54.165.187.107/")
#         driver.get("http://www.facebook.com/")
#         driver.quit()
#            
# object1=RunChrome()
# object1.test() 

'''page Load strategy to avoid the application closed suddenly'''
driverlocation = "C:\\Users\\skjag\\drivers\\chromedriver"
os.environ["webdriver.chrome.driver"]=driverlocation
driver_path = webdriver.Chrome(driverlocation)

caps = DesiredCapabilities.CHROME
 #caps["pageLoadStrategy"]="normal"
 #caps["pageLoadStrategy"]="eager"
caps["pageLoadStrategy"]="none"
options=webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")
options.add_argument("user-data-dir=C:\\Users\\skjag\\AppData\\Local\Google\\Chrome\\User Data\\")
driver=webdriver.Chrome(chrome_options=options)
driver.get("http://54.165.187.107/")
