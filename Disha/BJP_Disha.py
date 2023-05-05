from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select

class BJP(unittest.TestCase):
    def setUp(self) -> None:
        global driver, wait
        driver = webdriver.Chrome()
        wait= WebDriverWait(driver,20)
        driver.get("https://www.bjp.org/")

    def test_State(self):
        time.sleep(2)
        states_websites= driver.find_element(By.LINK_TEXT,"State Websites").click()
        time.sleep(2)
        states = driver.find_elements(By.XPATH,"//label[text()='Select State']/following-sibling::select/option")
        select_state = driver.find_element(By.XPATH,"//label[text()=Select State']/following-sibling::select")
        for state in states:
            if "D"in state.text:
                s= Select(select_state)
                s.select_by_visible_text(state.text)
                details = driver.find_elements(By.XPATH,"//h6[text()='State Office Details']/..//p[@class=""c-detail-address']")
                for detail in details:
                    if state.text==detail.text:
                        print(detail.text)
                    else:
                        continue
