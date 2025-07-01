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
driver.implicitly_wait(3),
driver.get(link)


element = driver.find_element(By.XPATH, '//div[@data-testid="tweetText"]')
text = element.text
print(text)



time.sleep(10)