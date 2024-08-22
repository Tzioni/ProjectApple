import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Project_Apple.Pages.AppleBaseSelenium import ProjectBaseSelenium
from Project_Apple.Pages.AppleGlobals import URL_BASE, LIMIT_1, LIMIT_2, ITEM_1, ITEM_3, ITEM_2
from Project_Apple.Pages.AppleProductPage import ProductPage
from Project_Apple.Pages.AppleHomePage import HomePage
from Project_Apple.Pages.AppleExplorePage import ExplorePage
from selenium.webdriver.support import expected_conditions as EC


"""
This class is responsible for executing the apple tests.
"""
class AppleTest(unittest.TestCase):
    """
    initialize Apple Test object
    """
    def setUp(self):
        self.base = ProjectBaseSelenium()
        self.driver = self.base.selenium_start(URL_BASE)
        self.homePageObject = HomePage(self.driver)
        self.explorePage = ExplorePage(self.driver)
        self.productPage = ProductPage(self.driver)

    """
    This test is responsible for finding the macbook price, and making sure the price is higher then the limit set.
    This test is a positive test.
    """
    def testSearchMacbook(self):
        self.homePageObject.createSearch("macbook")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, ITEM_1)))
        self.explorePage.selectItemMacbook()
        price = self.productPage.findPriceOfferMacbook()
        assert price>LIMIT_1,"the price is lower than 1400 not as expected"
    """
    This test is responsible for finding the airpods price, and making sure the price is lower then the limit set.
    This test is a negative test.
    """

    def testSearchAirpods(self):
        self.homePageObject.createSearch("airpods")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, ITEM_2)))
        self.explorePage.selectItemAirpods()
        price = self.productPage.findPriceOfferAirpods()
        assert price < LIMIT_2, "the price is higher than 150 not as expected"

    """
    This test is responsible for finding the iphone price, and making sure the price is higher then the limit set
    and lower then item1.
    This test is a negative test.
    """
    def testSearchIphone(self):
        self.homePageObject.createSearch("iphone")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, ITEM_3)))
        self.explorePage.selectItemIphone()
        price = self.productPage.findPriceOfferIphone()
        assert price > LIMIT_1, f"the price of {ITEM_3} is cheaper than {ITEM_1}"



    def tearDown(self):
        print ('into tear down')
        self.base.selenium_end(self.driver)

