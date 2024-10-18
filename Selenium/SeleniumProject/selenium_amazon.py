from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

link="https://www.amazon.com.tr/"

services=Service("./chromedriver.exe")
driver=webdriver.Chrome(service=services)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get(link)

driver.find_element(By.ID,"sp-cc-accept").click()

searchInput= driver.find_element(By.ID,"twotabsearchtextbox")
searchInput.click()
searchInput.send_keys("laptop")
searchInput.send_keys(Keys.ENTER)

def screenMove(moveID):
 move = driver.find_element(By.ID, moveID)
 actions = ActionChains(driver)
 actions.move_to_element(move).perform()

def filter(filterChoice):
 driver.find_element(By.XPATH, filterChoice).click()

moveID="p_n_feature_twenty-six_browse-bin-title"
screenMove(moveID)

filterChoice="//span[text()='Daha fazlasını gör']"
filter(filterChoice)
filterChoice="//span[text()='MONSTER']"
filter(filterChoice)
filterChoice="//span[text()='64 GB']"
filter(filterChoice)

names=driver.find_elements(By.XPATH,"//span[@class='a-size-base-plus a-color-base a-text-normal']")
for name in names:
 print(name.text)


time.sleep(5)

