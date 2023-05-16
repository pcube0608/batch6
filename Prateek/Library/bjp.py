from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from re import sub
driver = webdriver.Chrome()
driver.get("https://www.bjp.org/home")
driver.maximize_window()

time.sleep(5)
driver.find_element(By.CLASS_NAME,'statewebsite').click()
sel = Select(driver.find_element(By.ID,'edit-field-state-webites-sec-state-target-id'))

M_States = driver.find_elements(By.XPATH,"//option[starts-with(text(),'M')]")


def camel_case(s):
    s = sub(r"(_|-)+", " ", s).title()
    return ''.join([s[0].lower(), s[1:]])


for i in M_States:
    i.click()
    state = i.text
    state = camel_case(state)
    print(state)
    # address = driver.find_element(By.XPATH,"//img[contains(@src,'"+state+"')]/parent::div/following-sibling::div//p")
    address = driver.find_element(By.XPATH,"//p[contains(text(),'"+state+"')]")
    print(address)
    time.sleep(2)
