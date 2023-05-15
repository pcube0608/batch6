from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://amazon.in")

dropdownCategory = driver.find_element(By.ID,"searchDropdownBox")
OptionValueList = driver.find_elements(By.XPATH,"//select[@id='searchDropdownBox']/option")

OptionCount = len(OptionValueList)

sel = Select(dropdownCategory)
# sel.select_by_index(4)

## for bucket in tank
for i in range(OptionCount):
    print(i)
    sel.select_by_index(i)


time.sleep(30)