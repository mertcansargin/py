from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


link="https://www.trendyol.com/"

services=Service("./chromedriver.exe")
driver=webdriver.Chrome(service=services)
driver.maximize_window()
driver.get(link)


def findId(findId):
    findedID=driver.find_element(By.ID, findId)
    return findedID

def sendkey(find,args):
    findedID=findId(find)
    findedID.click()
    findedID.send_keys(args)

def clickID(find):
    findedID=findId(find)
    findedID.click()
#--------------------------------------------
def findXpath(findXpath):
    findedXpath=driver.find_element(By.XPATH, findXpath)
    return findedXpath

def clickXpath(findx):
    findedXpath=findXpath(findx)
    findedXpath.click()
#--------------------------------------------
def findName(findName):
    findedn=driver.find_element(By.NAME , findName)
    return findedn

def clickName(findn):
    findedName=findName(findn)
    findedName.click()



find="Rating-Review"
clickID(find)
find="onetrust-accept-btn-handler"
clickID(find)
findx="//p[text()='Giriş Yap']"
clickXpath(findx)
findx="//span[text()='Üye Ol']"
clickXpath(findx)
find="register-email"
args="email@email.com"
sendkey(find,args)
find="register-password-input"
args="Password1234"
sendkey(find,args)
findx="//span[text()='Erkek']"
clickXpath(findx)
findx="//div[text()='Tarafıma avantajlı tekliflerin sunulabilmesi amacıyla kişisel verilerimin işlenmesine ve paylaşılmasına']"
clickXpath(findx)
find="recaptcha-anchor-label"
clickID(find)
#findx="//span[text()='Tarafıma elektronik ileti gönderilmesini kabul ediyorum.']"
#clickXpath(findx)
#findx="//div[text()='Kişisel verilerimin işlenmesine yönelik']"
#clickXpath(findx)
findx="//span[text()='Üye Ol']"
clickXpath(findx)


time.sleep(60)




