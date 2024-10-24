from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

link="https://www.trendyol.com/giris?cb="

services=Service("./chromedriver.exe")
driver=webdriver.Chrome(service=services)
driver.maximize_window()
driver.get(link)

def findId(finedid):
    findedid=driver.find_element(By.ID,finedid)
    return findedid

def clickId(find):
    findedid=findId(find)
    findedid.click

def senkeyid(find,arg):
    findedid=findId(find)
    findedid.click()
    findedid.send_keys(arg)

#----------------------------

def findXpath(xpath):
    findedx=driver.find_element(By.XPATH,xpath)
    return findedx

def clickX(xpath):
    clickxpath = findXpath(xpath)
    clickxpath.click()  # Parantez eklendi
    print("tıklandı")




find="login-email"
arg="deneme123@gmail.com"
senkeyid(find,arg)
find="login-password-input"
arg="password123456"
senkeyid(find,arg)
xpath="//button[@type='submit']//span[text()='Giriş Yap']"
clickX(xpath)

try:
    error_div = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-box-wrapper"))
    )
    print("Hata Mesajı: ", error_div.text)

except:
    print("Hata mesajı bulunamadı.")
    

time.sleep(10)
