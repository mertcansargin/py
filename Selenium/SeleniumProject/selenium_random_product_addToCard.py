from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 
import random

productArray = ["elbise", "etek", "pijama", "pantolon"]
pArray=len(productArray)
productBeden=["S","M","L","XL"]

#tekrardan bir random fonk. yazmadan yerinde denemek istedim



link="http://lcw.com"


# lcw dan random bir ürün arayıp sepete ekleyecek 
# beden seçimide randol olabilir aslında

services=Service("./chromedriver.exe")
driver=webdriver.Chrome(service=services)
driver.maximize_window()
driver.get(link)


def randomSizes():
    deneme=driver.find_elements(By.XPATH,"//div[@id='option-size']/a")
    texts = [element.text for element in deneme]
    filtered_texts = list(filter(lambda text: text != "", texts))
    print(filtered_texts)
    pBArray=random.randint(0,len(filtered_texts)-1)
    randomsize=filtered_texts[pBArray]
    print("beden: ",randomsize)
    return randomsize

def randomNumber():
    rnd=random.randint(0,pArray-1)
    return rnd
#----------------------------------------------------
def findID(id):
    findedid=driver.find_element(By.ID,id)
    return findedid

def clickID(finid):
    clickedid=findID(finid)
    clickedid.click()

def sendKeyInput(id):
    rndprd=randomNumber()
    key=findID(id)
    key.click()
    key.send_keys(productArray[rndprd])
#------------------------------------------------------ 
def findX(findXpath):
    findedXpath=driver.find_element(By.XPATH,findXpath)
    return findedXpath

def clickFindX(fXpath):
    clickFX=findX(fXpath)
    clickFX.click()



  

id="cookieseal-banner-accept"
clickID(id)
id="search-form__input-field__search-input"
sendKeyInput(id)
fXpath="//button[text()='Ara']"
clickFindX(fXpath)
fXpath="//h5[@class='product-card__title']"
clickFindX(fXpath)
time.sleep(10)
randomsize=randomSizes()
fXpath="//a[text()='{}']".format(randomsize)
clickFindX(fXpath)
id="pd_add_to_cart"
clickID(id)

time.sleep(10)

