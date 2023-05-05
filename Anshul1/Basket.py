import time
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.support.select import Select

Basket = webdriver.Chrome()

Basket.get("https://www.bigbasket.com/ps/?q=vegetables")
time.sleep(2)

ShortBy=Basket.find_element(By.XPATH,"//*[contains(@id,'sel1')]")
list = Select(ShortBy)
list.select_by_index(2)
time.sleep(5)
CarrotPriceList=Basket.find_element(By.XPATH,"//*[contains(@class,'ng-scope open')]")
QyantityList = Select(CarrotPriceList)
QyantityList.select_by_index(1)
time.sleep(5)

