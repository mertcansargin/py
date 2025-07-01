from locators import baseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class baseFunc:
  services=Service(baseClass.chromedriverpath)
  driver=webdriver.Chrome(service=services)

  def openWindow(driver):
   driver.get(baseClass.link)


  def closeModal(driver):
    modal=(By.CLASS_NAME, '.modal-close')
    modal.click()


