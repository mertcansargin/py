
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from locators import baseClass
from functions import baseFunc


services=Service(baseClass.chromedriverpath)
driver=webdriver.Chrome(service=services)

baseFunc.openWindow(driver)
baseFunc.closeModal(driver)

time.sleep(10)