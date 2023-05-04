import time

from selenium import webdriver

import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class IPL1(unittest.TestCase):
    def setUp(self) -> None:
        global Ipl
        Ipl=webdriver.Chrome()
    def Matches(self):
        Ipl.get("https://www.iplt20.com/matches/schedule/men")
        Ipl.maximize_window()
        time.sleep(10)
        AllV=Ipl.find_element(By.XPATH,"//div[@class='customSelecBox openSBox']/child::div")
        AllV.click()
        AllVenue=Ipl.find_elements(By.XPATH,"//div[@ng-click='resultsfilterByGround(list,'Upcoming')']")
        for Venue in AllVenue:
            print(Venue.text)
        Match=Ipl.find_element(By.XPATH,"(//li[@class='active  has-children']/child::a)[2]")
        Match.click()
        time.sleep(10)
        Result=Ipl.find_element(By.XPATH,"(//li[@class='nav-item']/child::a)[2]")
        Ac=ActionChains(Ipl)
        Ac.move_to_element(Result).click().perform()
        time.sleep(10)
        Session=Ipl.find_element(By.XPATH,"//div[text()='SEASON 2023']")
        Session.click()
        Session2021=Ipl.find_element(By.XPATH,"//div[@class='cSBList active']/child::div[3]")
        Ac=ActionChains(Ipl)
        Ac.move_to_element(Session2021).click().perform()
        time.sleep(10)
        TimeDate=Ipl.find_elements(By.XPATH,"//div[@class='w50 fl']/child::div")
        for date in TimeDate:
            print(date.text)
    def Matches(self):
        Ipl.get("https://www.iplt20.com/matches/results/men/2020")
        Ipl.maximize_window()
        time.sleep(10)
        session=Ipl.find_element(By.XPATH,"//div[text()='SEASON 2023']")
        session.click()
        time.sleep(5)
        session2020=Ipl.find_element(By.XPATH,"//div[@class='cSBList active']/child::div[4]")
        Ac=ActionChains(Ipl)
        Ac.move_to_element(session2020).click().perform()
        time.sleep(10)
        Win=Ipl.find_elements(By.XPATH,"//div[@class=' w20 tl pr50']/child::div")
        for Winner in Win:
            print(Winner.text)
if __name__ == "__main__":
    unittest.main()





