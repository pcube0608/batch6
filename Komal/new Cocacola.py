from selenium import webdriver
import unittest
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cocacola(unittest.TestCase):

    def setUp(self) -> None:
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.coca-colacompany.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[text()='Confirm my Choices']").click()

    def test_Search(self):
        time.sleep(3)
        driver.find_element(By.XPATH,"//a[@id='searchIcon']").click()
        driver.find_element(By.XPATH,"//button[contains(@id,'btn_contentType')]").click()

        list_media_type = driver.find_elements(By.XPATH,"//li[@role='presentation']/a")

        count = len(list_media_type)
        wait = WebDriverWait(driver,10)
        for i in range(0,count-1):
            list_media_type[i].click()
            #time.sleep(4)

            wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='searchResult__title-container']/a")))
            list_EachMediaType=driver.find_elements(By.XPATH,"//div[@class='searchResult__title-container']/a")
            for eachMediaType in list_EachMediaType:
                url =eachMediaType.get_attribute('href')
                print(url)

            driver.find_element(By.XPATH, "//button[contains(@id,'btn_contentType')]").click()

    def test_ReciteMe(self):
        driver.find_element(By.ID,"recitemeIcon").click()

        wait = WebDriverWait(driver,10)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@title='Play']")))
        list_menuItems = driver.find_elements(By.XPATH,"//a[@class='cmp-navigation__item-link']")


        #for i in list_menuItems
        action = ActionChains(driver)
        for menu in list_menuItems:
            action.move_to_element(menu).perform()
            #         time.sleep(4)
