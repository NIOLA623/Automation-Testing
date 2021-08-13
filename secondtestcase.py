import unittest
from selenium import webdriver

# Aisha Idowu
# Task 22

def setUpModule():  # Executes before any class
    print('Setup Module')

def tearDownModule():
    print('Tear down Module')   # Executes after completing everything in the Python Module


class randomTest(unittest.TestCase):
    @classmethod
    def setUp(self):  # SetUp method: Executes (multiple times) before every other test methods
        print('setup test method')

    @classmethod
    def setUpClass(cls):  # setUpClass: Executes once before all other tests
        print('Opening Test cases')

    @classmethod
    def tearDownClass(cls):   # Executes once after all other tests
        print('Closing Test cases')

    def test_firstTest(self):
        print('First test method')

    def test_secondTest(self):
        print('Second test method')

    def test_thirdTest(self):
        print('Third test method')

    def test_fourthTest(self):
        print('Fourth test method')


    @classmethod
    def tearDown(self):   # tearDown: Executes (multiple times) after every other test methods
        print('Teardown method')




if __name__ == '__main__':  # To make the code run call the main method from the unit test module
    unittest.main()

