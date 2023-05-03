from selenium import webdriver
import unittest

class Automation(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://www.yatra.com")
        driver.maximize_window()
        #driver.implicitly_wait(15)

#click on Round trip
    def test_TestingClick(self):
        Element = driver.find_element_by_xpath("//a[contains(@title,'Round Trip')]")
        Element.click()

#select text box values
    def test_Validate_textbox(self):
        driver.find_element_by_xpath("//input[@id='BE_flight_origin_city']").send_keys("New Delhi")
        driver.find_element_by_xpath("//input[@id='BE_flight_arrival_city']").send_keys("Mumbai")
        driver.find_element_by_xpath("(//div[@class='view-return'])[2]//i")

#Expand the options
    def test_TestingClick(self):
        Element1 = driver.find_element_by_xpath("//div[@id='BE_flight_paxInfoBox']//i")
        Element1.click()

#select two adults
    def test_TestingClick(self):
        Element2 = driver.find_element_by_xpath("//span[@class='ddSpinnerPlus']")
        Element2.click()


   #def tearDown(self):
    #  driver.quit()

if __name__=='__main__':
    unittest.main()

