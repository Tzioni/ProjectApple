import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
This class is responsible for extracting the price of the product the website
the products are: macbook, airpods, iphone.
"""

class ProductPage():
    """
    initialize ProductPage object.
    """
    def __init__(self,driver):
        self.driver = driver
        self.findPriceMacbook = "p[class= 'welcome__lockup-primary-copy has-dynamic-content']"
        self.findPriceAirpods = "p[class='typography-compare-price pricing']"
        self.findPriceIphone = "p[class='welcome__lockup-primary-copy has-dynamic-content show']"
    """
    This method is responsible for extracting the price offer of macbook from the website.
    In addition this method is responsible for slicing the price offer and extracting the macbook price from it.
    """
    def findPriceOfferMacbook(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,self.findPriceMacbook)))
        time.sleep(3)  # added since sometimes we still have stability issues at this point
        priceOffer = self.driver.find_element(By.CSS_SELECTOR, self.findPriceMacbook)
        priceOfferText = priceOffer.text
        print(f'price found the value is {priceOfferText}')
        priceAsStr = priceOfferText
        index1=priceAsStr.index("or")-1
        index2 = priceAsStr.index("$")+1
        priceTemp = priceAsStr[index2:index1]
        time.sleep(3)
        print(priceTemp)
        price = int(priceTemp)
        return price

    """
    This method is responsible for extracting the price offer of airpods from the website.
    In addition this method is responsible for slicing the price offer and extracting the airpods price from it.
    """
    def findPriceOfferAirpods(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.findPriceAirpods)))
        time.sleep(3)  # added since sometimes we still have stability issues at this point
        priceOffer = self.driver.find_elements(By.CSS_SELECTOR, self.findPriceAirpods)
        priceOfferText = priceOffer[1].text
        print(f'price found the value is {priceOfferText}')
        priceAsStr = priceOfferText
        index1 = priceAsStr[-3:]
        priceTemp = index1
        time.sleep(3)
        print(priceTemp)
        price = int(priceTemp)
        return price

    """
    This method is responsible for extracting the price offer of iphone from the website.
    In addition this method is responsible for slicing the price offer and extracting the iphone price from it.
    """
    def findPriceOfferIphone(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.findPriceIphone)))
        time.sleep(3)  # added since sometimes we still have stability issues at this point
        priceOffer = self.driver.find_element(By.CSS_SELECTOR, self.findPriceIphone)
        priceOfferText = priceOffer.text
        print(f'price found the value is {priceOfferText}')
        priceAsStr = priceOfferText
        index1 = priceAsStr.index("or") - 1
        index2 = priceAsStr.index("$") + 1
        priceTemp = priceAsStr[index2:index1]
        time.sleep(3)
        print(priceTemp)
        price = int(priceTemp)
        return price
