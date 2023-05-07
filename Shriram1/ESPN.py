import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class ESPN(unittest.TestCase):

    def setUp(self) -> None:
        global driver
        driver=webdriver.Chrome()
        driver.get("https://www.espncricinfo.com/")
        driver.maximize_window()

    def test_Ipl2023(self):
        driver.implicitly_wait(30)

        series = driver.find_element(By.XPATH,"(//div[@class='ds-popper-wrapper']/child::a)[2]")
        action = ActionChains(driver)
        action.move_to_element(series).perform()
        time.sleep(2)
        ipl2023 = driver.find_element(By.XPATH,"//li[@title='Indian Premier League 2023']/a")
        ipl2023.click()
        driver.find_element(By.ID,"wzrk-confirm").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//span[contains(@class,'primary ds-bo')]").click()
        #time.sleep(4)
        mi = driver.find_element(By.XPATH,"//div[contains(@class,'ds-text-typo ds-my-1')]/child::div")
        actMI = ActionChains(driver)
        actMI.move_to_element(mi).click().perform()
        #time.sleep(5)
        scorecard = driver.find_element(By.XPATH,"//span[text()='Scorecard']/parent::a")
        print(scorecard.get_attribute("href"))
        #time.sleep(5)
        outplayers = driver.find_elements(By.XPATH,"//td[@class='ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-flex ds-items-center']/descendant::span/span")


        for player in outplayers:
            print(player.text)

    def tearDown(self) -> None:
        driver.quit()

if __name__=="__main__":
    unittest.main()
