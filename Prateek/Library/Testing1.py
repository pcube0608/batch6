import unittest
from selenium import webdriver

class Testing1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("before class")

    def setUp(self) -> None:
        print("before test")

    def test_abc(self):
        print("testing abc")

    def test_xyz(self):
        print("testing xyz")

    def tearDown(self) -> None:
        print("after test")

    @classmethod
    def tearDownClass(cls) -> None:
        print("after class")