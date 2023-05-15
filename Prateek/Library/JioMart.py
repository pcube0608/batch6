from selenium import webdriver
import unittest
import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class JioMart(unittest.TestCase):


    def setUpClass(cls) -> None:
        print("I am running before class execution")

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://jiomart.com")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_FurnitureProducts(self):
        driver.find_element(By.ID,"ham_close").click()
        driver.find_element(By.XPATH,"//span[text()='Shop By Category']").click()
        time.sleep(5)
        ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//div[contains(text(),'Furniture')])[17]")).perform()
        driver.find_element(By.XPATH,"(//div[contains(text(),'Furniture')])[17]").click()
        driver.find_element(By.XPATH,"//div[@data-target='#sub-category-13452']").click()
        driver.find_element(By.XPATH,"//div[starts-with(text(),' Chairs')]").click()


        driver.find_element(By.XPATH,"(//img[@class='collapse-toggle'])[8]").click()
        driver.find_element(By.XPATH,"//div[contains(text(),'High to Low')]").click()
        wait = WebDriverWait(driver,10)
        time.sleep(5)
        ChairNameList = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'plp-card-details-name')]")))
        ChairPriceList = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//span[contains(@class,'jm-heading-xxs')]")))
        d = {}
        d1 = {}
        for i in range(12):
            ChairNameList = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'plp-card-details-name')]")))
            ChairName = ChairNameList[i].text
            ChairPriceList = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//span[contains(@class,'jm-heading-xxs')]")))
            ChairPrice = ChairPriceList[i].text
            d[ChairName] = ChairPrice
            ChairNameList[i].click()
            articleNo = driver.find_element(By.XPATH,"//section[contains(@class,'product-article-detail')]//span").text
            # d1[articleNo] = ChairPrice
            d[articleNo] = d[ChairName]
            del d[ChairName]
            driver.back()
            time.sleep(3)
            driver.refresh()
            time.sleep(3)

        print(d)
        # print(d1)

    def test_Household(self):
        pass

    def tearDown(self) -> None:
        print("teardown")

    def tearDownClass(cls) -> None:
        print("at last of all Tests")

if __name__ == '__main__':
    unittest.main()

