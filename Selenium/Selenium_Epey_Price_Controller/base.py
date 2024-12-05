from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time 
from locators import parameters
from locators import productpage

from selenium.webdriver.common.by import By
from fonctions import baseClass


def runTask():
   

    driver = webdriver.Chrome()
    base = baseClass(driver)
    
    def main():
        try:
         driver.get(parameters.link)
         driver.maximize_window()

         #base.screenMove(productpage.scrolForProduct)         
         base.click(productpage.cookieclose)
         base.click(productpage.phoneColor)

         current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         print(f"Sistem Saati: {current_time}")

         price = base.get_clean_prices_as_array(productpage.phonefiyat)
         for text in price[:3]:
          print("Fiyat:", text)
         time.sleep(5)

        finally:
         print("----------------------------")
        print("Bir sonraki çalışma için bekleniyor...")
        time.sleep(5 * 60)  # 15 dakika bekle
        main()  # Selenium görevi çalıştır
    main()


runTask()