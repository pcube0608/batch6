from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time


driver= webdriver.Chrome()
driver.get("https://www.iplt20.com/matches/schedule/men")
action = ActionChains(driver)
driver.maximize_window()
time.sleep(3)

accept_cookies = driver.find_element(By.XPATH,"//button[text()='Accept cookies']").click()
time.sleep(2)

all_venues = driver.find_element(By.XPATH,"//div[contains(text(),'All Venues')]").click()
all_venues_list = driver.find_elements(By.XPATH,"//div[@class='cSBList active']/div[@class='cSBListItems ng-binding ng-scope']")
count = len(all_venues_list)
venues_list=[]
for i in range(count):
    venues_list.append(all_venues_list[i].text)
print(venues_list)
time.sleep(2)

all_matches = driver.find_elements(By.XPATH,"//div[@class='vn-matchDate ng-binding']")
count1 = len(all_matches)
matches_list=[]
for i in range(count1):
    matches_list.append(all_matches[i].text)
print(matches_list)
time.sleep(2)

matches= driver.find_element(By.XPATH,"(//a[text()='MATCHES'])[2]").click()
time.sleep(2)
results = driver.find_element(By.XPATH,"//a[text()='RESULTS']").click()
time.sleep(2)

results_list= driver.find_elements(By.XPATH,'//div[@class="vn-ticketTitle ng-binding ng-scope"]')
count2=len(results_list)
match_results=[]

for i in range(count2):
    match_results.append(results_list[i].text)
print(match_results)

