
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from locators import baseClass
from functions import baseFunc

baseFunc.openWindow(baseFunc.driver)
baseFunc.closeModal(baseFunc.driver)



time.sleep(10)