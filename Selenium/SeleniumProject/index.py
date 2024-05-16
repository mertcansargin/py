from selenium import webdriver
from selenium.webdriver.chrome.service import Service

services=Service("./chromedriver.exe")
driver=webdriver.Chrome(service=services)
driver.get("https://www.youtube.com/watch?v=ySLc8gZ3oEc&list=RDySLc8gZ3oEc&start_radio=1&ab_channel=ElectromaMV")
link=driver.current_url
baslik=driver.title
print("şu anki link: "+link)
print("şu anki baslik: "+baslik)