from selenium.webdriver.common.by import By




class parameters:
    link="https://www.epey.com/akilli-telefonlar/apple-iphone-13.html"
    chromedriver="./chromedriver.exe"
    # searchtext='iphone 13 128'


#class main_page_locators:
    #  searchbar_id=(By.ID,'Ara')
    # searchbutton_id=(By.ID,'submit')

class productpage:
    phonefiyat=(By.XPATH, "//span[@class='urun_fiyat']")
    phoneColor=(By.XPATH, "//label[input[@value='Beyaz']]")
    scrolForProduct=(By.ID, "urunfiltre")
    cookieclose=(By.ID,"cookie_agree")
