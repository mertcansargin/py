from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


link="https://x.com/pusholder"
driverpath="./chromedriver.exe"
cssValue='css-1jxf684'

services=Service(driverpath)
driver=webdriver.Chrome(service=services)
driver.maximize_window()
driver.implicitly_wait(5),
driver.get(link)


elements = driver.find_elements(By.XPATH, '//div[@data-testid="tweetText"]')
time_elements = driver.find_elements(By.TAG_NAME, "time")

print('Element: ',len(elements))
print('Time: ',len(time_elements))

for element in elements:
    for time_element in time_elements:
     print(element.text)
     print(time_element.text)
     print("--------------------------------------------------------")
     break

 
time.sleep(10)