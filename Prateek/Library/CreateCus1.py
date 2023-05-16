import string

from selenium import webdriver
import unittest
import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreateCus1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(15)

    def setUp(self) -> None:
        driver.get("https://org91296e38.crm8.dynamics.com/main.aspx")
        driver.maximize_window()
        email = "pcubeworkforce@gmail.com"
        password = "Salesforce"
        driver.find_element(By.NAME, 'loginfmt').send_keys(email)
        time.sleep(3)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(3)
        driver.find_element(By.NAME, 'passwd').send_keys(password)
        driver.find_element(By.ID, "idSIButton9").click()
        driver.find_element(By.ID, "idSIButton9").click()

        frameElement = driver.find_element(By.ID, "AppLandingPage")
        driver.switch_to.frame(frameElement)
        driver.find_element(By.ID, "AppModuleTileSec_1_Item_1").click()

    def test_CreateLead(self):
        topic_list = ['Teleco','Finance','Insurance']
        N=7
        lastName = ''.join(random.choices(string.ascii_letters, k=N))
        time.sleep(10)
        driver.find_element(By.ID,"quickCreateLauncher_buttoncrm_header_global$button").click()
        driver.find_element(By.XPATH,"//*[text()='Lead']").click()
        driver.find_element(By.XPATH,'//input[@aria-label="Topic"]').send_keys(random.choice(topic_list))
        driver.find_element(By.XPATH,'//input[@aria-label="Last Name"]').send_keys(lastName)
        driver.find_element(By.XPATH, "//button[contains(@id,'quickCreateSaveAndCloseBtn')]").click()
        time.sleep(2)
        wait = WebDriverWait(driver,10)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[text()='View Record']")))
        driver.find_element(By.XPATH, "//p[text()='View Record']").click()
        driver.find_element(By.XPATH, '//button[@aria-label="Save & Close"]').click()

    def test_SearchAndConverToOpportunity(self):
        driver.find_element(By.XPATH,"//span[text()='Leads']").click()
        driver.find_element(By.XPATH,"//input[@aria-label='Lead Filter by keyword']").send_keys("test")
        driver.find_element(By.XPATH,"//input[@aria-label='Lead Filter by keyword']").send_keys(Keys.ENTER)
        driver.find_element(By.XPATH,'//div[@aria-rowindex="2"]//a[@aria-label="test"]').click()

        driver.find_element(By.XPATH,"//button[@aria-label='Qualify']").click()
        driver.find_element(By.XPATH,"//button[contains(@id,'opportunity.Save')]").click()
        driver.find_element(By.XPATH,"//*[text()='Save & Close']").click()



    def tearDown(self) -> None:
        driver.quit()

if __name__ == "__main__":
    unittest.main()

