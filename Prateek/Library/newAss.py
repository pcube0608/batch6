from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://www.maths.surrey.ac.uk/explore/nigelspages/htmltry.htm")
driver.maximize_window()

textarea = driver.find_element(By.XPATH,"//textarea[@name='text']")
driver.execute_script("document.getElementsByName('text')[0].setAttribute('rows','100')")
# ac = ActionChains(driver)
# ac.click_and_hold(textarea).move_to_element_with_offset(textarea,-120,-100).release().perform()

time.sleep(30)