from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&Locality=Wakad&cityName=Pune")
# driver.implicitly_wait(30)
time.sleep(5)
PropertyList = driver.find_elements(By.XPATH,"//div[contains(@class,'card__info')]/h2")
print(len(PropertyList))
#
# driver.find_element(By.CLASS_NAME,"close_chat_box").click()
# driver.find_element(By.CLASS_NAME,"sb_yes_btn").click()

act = ActionChains(driver)
wait = WebDriverWait(driver,10)
for prop in PropertyList:
    # time.sleep(1)
    print(prop.text)





# handlelist = driver.window_handles
#
# for handle in handlelist:
#
#     driver.switch_to.window(handle)
#     if driver.title == "Loksabha":
#         pass
#         ### profile
#         ### speaker's Name
#     else:
#         continue