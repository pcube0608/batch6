from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()

driver.get("https://amazon.in")

action = ActionChains(driver)
BuyItAgain = driver.find_element(By.XPATH,"//h2[@class='a-color-base']")

action.move_to_element(BuyItAgain).perform()

BuyItAgain.click()



















Dropdown = driver.find_element(By.ID,"searchDropdownBox")

sel = Select(Dropdown)
sel.select_by_index(0)
########## LOOP ###########

## For bucket in tank

for i in range(4,200):
    print(i)
    sel.select_by_index(i)

time.sleep(20)


