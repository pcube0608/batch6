from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://support.sharekhan.com/faq")

driver.maximize_window()

driver.find_element(By.ID,"name").send_keys("terer")
time.sleep(23)