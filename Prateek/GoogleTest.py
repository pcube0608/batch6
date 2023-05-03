from selenium import webdriver
import unittest

class GoogleTest(unittest.TestCase):

    def setUp(self) -> None:
        global driver
        driver = webdriver.Chrome()
        driver.get("https://google.com")
        print("I am in Setup")

    def test_SearchResult(self):
        print("I am in SearchResult")

    def test_TImageSearch(self):
        print("I am in ImageResult")

    def test_FlightSearch(self):
        print("I am in FlightResult")

    def tearDown(self) -> None:
        driver.quit()
