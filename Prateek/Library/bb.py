from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://www.bigbasket.com/ps/?q=vegetables")
driver.implicitly_wait(30)
driver.maximize_window()

dropdownSort = driver.find_element(By.ID,"sel1")
sel = Select(dropdownSort)
# time.sleep(2)
sel.select_by_index(2)  ### Price High to Low
# time.sleep(5)
sel.select_by_value("string:alpha")   #### Name alphatical
# time.sleep(5)
wait = WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.XPATH,"//option[text()='Rupee Saving - Low to High']")))
sel.select_by_visible_text("Rupee Saving - Low to High")
time.sleep(30)