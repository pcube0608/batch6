import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ESPN(unittest.TestCase):

    def setUp(self) -> None:
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.espncricinfo.com/")
        driver.implicitly_wait(10)

    def test_Search(self):
        wait = WebDriverWait(driver, 15)
        # click on series
        series = driver.find_element(By.XPATH, "//a[text()='Series']")
        Action = ActionChains(driver)
        Action.move_to_element(series).perform()
        # click on IPL 2023
        driver.find_element(By.XPATH, "//li[@class='ds-w-full ds-flex']//span[text()='IPL 2023']").click()

        # close the timer pop-up windows after switch frame
        driver.switch_to.frame("google_ads_iframe_21783347309/espn.cricinfo.com/series_0")
        driver.find_element(By.XPATH, "//a[@onkeypress='javascript:closeOverlay();']").click()
        # switch to default frame
        driver.switch_to.default_content()
        # click on results to get last played match details
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Results']"))).click()
        # click on the last played match
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ds-text-compact-xxs']//div[contains(@class,'ds-pb-3')]"))).click()
        # close the timer pop-up windows after switch frame
        driver.switch_to.frame("google_ads_iframe_21783347309/espn.cricinfo.com/game/scorecard_0")
        driver.find_element(By.XPATH, "//a[@onkeypress='javascript:closeOverlay();']").click()
        # switch to default frame
        driver.switch_to.default_content()
        # Validate the url
        print(driver.current_url)

        # print the players names who got out in this match
        Out_List = driver.find_elements(By.XPATH, "//td[@class='ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-flex ds-items-center']/a")
        for elem in Out_List:
            print(elem.get_attribute("title"))
