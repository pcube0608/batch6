import unittest
from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class CreateC(unittest.TestCase):

    def test_CreateLead(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://org91296e38.crm8.dynamics.com/")
        # time.sleep(1)
        driver.find_element(By.ID,"i0116").send_keys("pcubeworkforce@gmail.com")
        # time.sleep(1)
        driver.find_element(By.ID,"idSIButton9").click()
        time.sleep(3)
        driver.find_element(By.ID, "i0118").send_keys("Salesforce")
        time.sleep(1)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(1)
        driver.find_element(By.ID, "idSIButton9").click()
        # time.sleep(10)
        driver.switch_to.frame(driver.find_element(By.ID,"AppLandingPage"))

        driver.find_element(By.ID,"AppDetailsSec_1_Item_1").click()
        # time.sleep(3)
        driver.switch_to.default_content()
        # time.sleep(5)
        driver.find_element(By.ID,"quickCreateLauncher_buttoncrm_header_global$button").click()
        # time.sleep(3)
        driver.find_element(By.XPATH,"//*[text()='Lead']").click()
        # driver.find_element(By.ID,"id-823").click()

        driver.find_element(By.XPATH,"//input[contains(@id,'subject')]").send_keys("Mr")
        driver.find_element(By.XPATH,'//input[@aria-label="Last Name"]').send_keys("TestPrtk1")
        driver.find_element(By.ID, "quickCreateSaveAndCloseBtn_1").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Leads']").click()

        driver.find_element(By.ID,"quickFind_text_2").send_keys("TestPrtk1")
        driver.find_element(By.ID,"quickFind_text_2").send_keys(Keys.ENTER)
        driver.find_element(By.XPATH,"//*[text()='TestPrtk1']").click()
        driver.find_element(By.XPATH,'//button[@aria-label="Qualify"]').click()
        driver.find_element(By.ID,'opportunity|NoRelationship|Form|Mscrm.Form.opportunity.Save.Menu$splitButtonId_button4$button').click()
        driver.find_element(By.XPATH, "//*[text()='Save & Close']").click()

        driver.quit()

