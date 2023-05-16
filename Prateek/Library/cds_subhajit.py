import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.cds.com/")
driver.implicitly_wait(10)

# Print the title of the webpage.
print(driver.title)

# Scroll down up to Terms & Conditions.
Terms_Conditions = driver.find_element(By.XPATH, "//a[contains(text(),'Built with Volusion')]")
action = ActionChains(driver)
action.move_to_element(Terms_Conditions).perform()

# Performing click on All Products option.
ClickTo_AllProducts = driver.find_element(By.XPATH, "//a[contains(text(),'All Products')]")
ClickTo_AllProducts.click()

# Print the Current URL.
print(driver.current_url)

# hover mouse to Repair Information using ActionChains Class.
Repair_Information = driver.find_element(By.XPATH, "(//a[contains(text(),'Repair Information')])[3]")
action = ActionChains(driver)
action.move_to_element(Repair_Information).perform()

# Performing click on Maintenance and Repairs.
ClickToMaintenance_Repairs = driver.find_element(By.XPATH, "(//a[contains(text(), 'Maintenance and Repairs')])[2]")
ClickToMaintenance_Repairs.click()

# Scroll up to shopping button.
Shopping = driver.find_element(By.XPATH, "//span[contains(text(), 'SHOPPING')]")
action = ActionChains(driver)
action.move_to_element(Shopping).perform()

# Print No of days in console.
No_days = driver.find_element(By.XPATH, "//span[contains(text(), '30 Days.')]")
print(No_days.text)

# Scroll up to CD,DVD,Blu-ray Media.
BluRay_Media = driver.find_element(By.XPATH, "(//a[contains(text(),'CD, DVD, Blu-Ray Media')])[3]")
action = ActionChains(driver)
action.move_to_element(BluRay_Media).perform()

# performing click on disk and USB Packaging.
USB_Packaging = driver.find_element(By.XPATH, "(//a[contains(text(), 'Disc and USB Packaging')])[3]")
USB_Packaging.click()

# scroll up to FlashPad USB Flash Drive Packaging
FlashPad_USB = driver.find_element(By.XPATH, "//span[@itemprop= 'name']")
action = ActionChains(driver)
action.move_to_element(FlashPad_USB).perform()

# select price Low to High.
Sort_By = driver.find_element(By.ID,"SortBy")
Sel = Select(Sort_By)
Sel.select_by_visible_text("Price: Low to High")