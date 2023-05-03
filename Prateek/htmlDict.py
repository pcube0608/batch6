from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit")
userpass = {"Prateek":"L","Minaj":"Atar"}
for key,value in userpass.items():
    driver.find_element(By.ID, "runbtn").click()

    driver.switch_to.frame(driver.find_element(By.ID,"iframeResult"))
    driver.find_element(By.ID,"fname").clear()
    driver.find_element(By.ID,"fname").send_keys(key)
    driver.find_element(By.ID,"lname").clear()
    driver.find_element(By.ID,"lname").send_keys(value)

    driver.find_element(By.XPATH,"//input[@type='submit']").click()
    time.sleep(3)
    
    driver.switch_to.default_content()

