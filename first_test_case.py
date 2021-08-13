import unittest
from selenium import webdriver

# Aisha Idowu
# Task 22


class linuxjobberTest(unittest.TestCase):  # Test case created
    def test_chatscrum(self):   # Test Method defined
      self.driver = webdriver.Chrome(executable_path='C:\Web Drivers\chromedriver.exe')
      self.driver.get('https://chatscrum.com')
      print('The title of the page is', self.driver.title)
      self.driver.close()

    def test_workntutor(self):
        self.driver = webdriver.Chrome(executable_path='C:\Web Drivers\chromedriver.exe')
        self.driver.get('http://workntutor.com')
        print('The title of the page is', self.driver.title)
        self.driver.close()


if __name__ == '__main__':  # To make the code run call the main method from the unit test module
    unittest.main()