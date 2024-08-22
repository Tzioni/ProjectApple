from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver


"""
This class is responsible for organizing the Selenium code lines.
"""
class ProjectBaseSelenium():



    def selenium_start(self,url):
        print('test start')
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get(url)
        driver.maximize_window()
        return driver



    def selenium_end(self, driver):
        driver.close()
        print('test end')