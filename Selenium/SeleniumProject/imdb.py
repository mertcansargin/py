from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

services=Service("./chromedriver.exe")
driver=webdriver.Chrome(service=services)
driver.maximize_window()
driver.get("https://www.imdb.com/")
driver.find_element(By.ID,"imdbHeader-navDrawerOpen").click()
driver.find_element(By.XPATH, "//span[text()='Top 250 TV Shows']").click()
