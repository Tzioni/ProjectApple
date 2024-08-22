import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

"""
This class is responsible for searching products in Apple Home Page
"""
class HomePage():
    """
    initialize HomePage object
    """
    def __init__(self,driver):
        self.driver = driver
        self.searchIcon = 'globalnav-menubutton-link-search'
        self.searchBox = "input[class='globalnav-searchfield-input']"




    """
    This method is responsible for opening the Search Box, typing in the desired product, and clicking Enter to search.
    """
    def createSearch(self,search_text):
        searchIcon = self.driver.find_element(By.ID, self.searchIcon)
        searchIcon.click()
        searchBox = self.driver.find_element(By.CSS_SELECTOR, self.searchBox)
        time.sleep(3)
        searchBox.send_keys(search_text)
        searchBox.send_keys(Keys.ENTER)
