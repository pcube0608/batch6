from selenium import webdriver
import unittest


def setUpModule():
    print("This is before all classes")

def tearDownModule():
    print("After all classes run")

class Assertion(unittest.TestCase):

    def setUpClass(cls) -> None:
        print("This is before Class Assertion")

    def tearDownClass(cls) -> None:
        print("This is after Class Assertion")

    @unittest.skip("Skipping this TC, as it is deferred")
    def test_case01(self):
        my_str = "Akarsh"
        my_roll = 123
        self.assertTrue(isinstance(my_str,str))
        self.assertTrue(isinstance(my_roll,int))
        self.fail()
        # title = driver.title
        # self.assertTrue(title=="Loksabha")
        # self.assertTrue(1==2)

    def test_case02(self):
        pi = 3.14
        self.assertFalse(isinstance(pi,int))

    def test_case03(self):
        pi = 3.14
        self.assertFalse(isinstance(pi,int))

class Assertion1(unittest.TestCase):

    def setUpClass(cls) -> None:
        print("This is before Class Assertion1")
    def test_case04(self):
        my_str = "Akarsh"
        my_roll = 123
        self.assertTrue(isinstance(my_str,str))
        self.assertTrue(isinstance(my_roll,int))
        # title = driver.title
        # self.assertTrue(title=="Loksabha")
        # self.assertTrue(1==2)


unittest.main(verbosity=2)