from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()

driver.get("https://www.americangolf.co.uk/")
driver.maximize_window()

wait = WebDriverWait(driver,10)
AcceptButton = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Accept']")))

# AcceptButton = driver.find_element(By.XPATH,"//button[text()='Accept']")
AcceptButton.click()

wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='header-navigation-left']/ul/li/a")))

MenuCategoryList = driver.find_elements(By.XPATH,"//div[@class='header-navigation-left']/ul/li/a")
count = len(MenuCategoryList)

url_List = []
action = ActionChains(driver)
for i in range(0,count):
    action.move_to_element(MenuCategoryList[i]).perform()
    if 'brands' in MenuCategoryList[i].get_attribute('href'):
        continue
    elif i<11:
        wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='header-navigation-left']/ul/li//img)["+str(i+1)+"]")))


    url = MenuCategoryList[i].get_attribute('href')
    url_List.append(url)

print(url_List)

for url1 in url_List:
    driver.get(url1)
    print(driver.title)
