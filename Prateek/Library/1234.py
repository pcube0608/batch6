
import unittest
import test123

class Abc(unittest.TestCase):

    def test_tt(self):
        print("I am in test1")

    def test_tt1(self):
        print("I am in test2")

a=7
print(a)
unittest.main(verbosity=2)