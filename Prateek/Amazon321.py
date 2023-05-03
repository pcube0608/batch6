from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

driver.get("https://amazon.in")

DropdownCategory = driver.find_element(By.ID,'searchDropdownBox')

sel = Select(DropdownCategory)

#for bucket in tank:
# for i in range(0,43):
#     sel.select_by_index(i)

### 1. We create list of webelements --> Xpath with multiple results [ find_elements ]
### 2. We used len function of python - It gives no of elements / entities in a list

ListWebelements = driver.find_elements(By.XPATH,"//select[@id='searchDropdownBox']/child::option")
# ListWebelements = [e1, el2, el3.......]
CategoryCount = len(ListWebelements)

## for bucket in tank

for elem in ListWebelements:
    if elem.text != "Deals":
        print(elem.text)
        elem.click()

driver.cu
time.sleep(30)
