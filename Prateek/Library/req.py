from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get("https://reqres.in")
method = driver.find_elements(By.XPATH,"//div[@class='endpoints']//li")
endpoints = driver.find_elements(By.XPATH,"//div[@class='endpoints']//li/a")
dic = {}
for i in range(0,15):
    meth = method[i].get_attribute('data-http')
    dic[meth] = endpoints[i].get_attribute('href')
    if meth == "get":
        res = requests.get(dic[meth])
        print(res.text)
    elif meth == "post":
        payload = {}
        requests.post(dic[meth],body=payload)
    else:
        print(dic.keys())
    del dic[meth]


