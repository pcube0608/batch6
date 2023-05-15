from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.bigbasket.com/ps/?q=vegetables")

driver.maximize_window()

wait = WebDriverWait(driver,10)

wait.until(EC.element_to_be_clickable((By.ID,"sel1")))

DropdownElement = driver.find_element(By.ID,"sel1")
sel = Select(DropdownElement)

sel.select_by_visible_text("Price - Low to High")

wait2 = WebDriverWait(driver,20)
wait2.until(EC.element_to_be_clickable((By.XPATH,"//option[text()='Price - Low to High' and @selected='selected']")))



wait1 = WebDriverWait(driver,100)
wait1.until(EC.element_to_be_clickable((By.XPATH,"(//span[contains(text(),'MAGGI')]/parent::label//i)[3]")))

MaggiCheckbox = driver.find_element(By.XPATH,"(//span[contains(text(),'MAGGI')]/parent::label//i)[3]")
MaggiCheckbox.click()

time.sleep(30)
