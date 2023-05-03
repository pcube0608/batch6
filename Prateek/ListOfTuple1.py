from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/howto/howto_css_contact_form.asp")

driver.maximize_window()

ContactFormData = [('Amarjeet','D','Australia'),('komal','D','Canada'),('Disha','B','USA')]
Fname = driver.find_element(By.ID,"fname")
LName = driver.find_element(By.ID,"lname")
Country = driver.find_element(By.NAME,'country')
Submit = driver.find_element(By.LINK_TEXT,"Submit")

sel = Select(Country)


for formData in ContactFormData:
    Fname.clear()
    LName.clear()
    Fname.send_keys(formData[0])
    LName.send_keys(formData[1])
    sel.select_by_visible_text(formData[2])

    Submit.click()


time.sleep(6)

