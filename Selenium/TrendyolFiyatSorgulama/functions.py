from locators import baseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class baseFunc:
 

  def openWindow(driver):
   driver.get(baseClass.link)


  def closeModal(driver):
    modal=(By.CLASS_NAME, '.modal-close')
    modal.click()