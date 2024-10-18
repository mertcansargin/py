from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

services=Service("./chromedriver.exe")
driver=webdriver.Chrome(service=services)
driver.maximize_window()
driver.get("https://www.imdb.com/")
driver.find_element(By.ID,"imdbHeader-navDrawerOpen").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='Top 250 TV Shows']").click()

