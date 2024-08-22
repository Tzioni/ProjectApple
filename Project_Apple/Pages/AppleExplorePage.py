import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Project_Apple.Pages.AppleGlobals import ITEM_1, ITEM_2, ITEM_3, ITEM_TYPE

"""
this class is responsible for selecting the chosen items from explore page.
the items are: macbook, airpods, iphone
"""
class ExplorePage():
    """
    initialize ExplorePage object
    """
    def __init__(self,driver):
        self.driver = driver


    """ 
    this method is responsible for selecting macbook from the item list in explore page.
    """
    def selectItemMacbook(self):
        clickItem = self.driver.find_elements(By.PARTIAL_LINK_TEXT,ITEM_1)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(clickItem[0]))
        clickItem[0].click()
    """
    this method is responsible for selecting airpods from the item list in explore page.
    """
    def selectItemAirpods(self):
        clickItem = self.driver.find_elements(By.PARTIAL_LINK_TEXT,ITEM_2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(clickItem[-2]))
        clickItem[-2].click()
    """
    this method is responsible for selecting iphone from the item list in explore page.
    """

    def selectItemIphone(self):
        clickItem = self.driver.find_elements(By.PARTIAL_LINK_TEXT,ITEM_3)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(clickItem[0]))
        clickItem[0].click()
        time.sleep(5)
        clickIcon = self.driver.find_element(By.CSS_SELECTOR,ITEM_TYPE)
        clickIcon.click()