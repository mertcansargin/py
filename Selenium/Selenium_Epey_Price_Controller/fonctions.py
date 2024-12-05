from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from locators import productpage




class baseClass:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 90)
    
    def click(self, selector):
        self.wait.until(ec.element_to_be_clickable(selector)).click()

    def input(self, selector, parameters):
        self.wait.until(ec.presence_of_element_located(selector)).send_keys(parameters)

    def wait_element(self, selector):
        return self.wait.until(ec.presence_of_element_located(selector))
    
    def scroll_into_view(self, selector):
        """Belirli bir elementi görünür hale getirmek için kaydır."""
        element = self.wait_element(selector)  # Elementin yüklenmesini bekle
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)


    def screenMove(self,moveID):
        move = self.driver.find_element(*moveID)
        actions = ActionChains(self.driver)
        actions.move_to_element(move).perform()


    def get_clean_prices_as_array(self, selector, exclude_text="Ücretsiz Kargo"):
     elements = self.driver.find_elements(*selector)
     prices = []
     for element in elements:
        full_text = element.text.split('\n')[0].strip()  # İlk satırı al ve boşlukları temizle
        if exclude_text not in full_text:
            prices.append(full_text)
     return prices



    def get_value_array(self, selector, exclude_text="Ücretsiz Kargo"):
     elements = self.driver.find_elements(*selector)
     prices = []
     for element in elements:
        full_text = element.text.split('\n')[0].strip()  # İlk satırı al ve boşlukları temizle
        if exclude_text not in full_text:
            prices.append(full_text)
     return prices
