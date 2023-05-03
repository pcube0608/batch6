from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("https://www.americangolf.co.uk/")

driver.maximize_window()
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Accept']"))).click()
time.sleep(3)
# listElem = driver.find_elements(By.XPATH,"//a[@class='a-level-1']")
listElem = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"//a[@class='a-level-1']")))


act = ActionChains(driver)
# for elem in listElem:
#     print(elem.text)
#     # if (elem.text).strip() == "BRANDS":
#     if "BRANDS" in elem.text:
#         continue
#     else:
#         act.move_to_element(elem).perform()
#         WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,'flyout-right')]//img")))
#         time.sleep(1)

## //div[@class='header-navigation-left']//a[@class='a-level-1']
pageLinks = []
ElemCount = len(listElem)
for i in range(ElemCount):
    if listElem[i].text in "BRANDS":
        continue
    else:
        act.move_to_element(listElem[i]).perform()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "(//div[contains(@class,'flyout-right')]//img)["+str(i)+"]")))
        pageLinks.append(listElem[i].get_attribute('href'))

print(pageLinks)
for link in pageLinks:
    driver.get(link)
    print(driver.title)