from selenium import webdriver
import time
import unittest

# Aisha Idowu
# Task 23

def setUpModule():
    global email
    global password
    global project
    global driver
    email = "idowumofolorunsho@gmail.com"
    password = "DearChat23%"
    project = "web-driver commands"

class SecondTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Opening Test Cases')
    @classmethod
    def tearDownClass(cls):
        print('Closing test cases')


    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\Web Drivers\chromedriver.exe')

    def test_one(self):
      self.driver.get('https://chatscrum.com')
      print('The title of the page is', self.driver.title)
      time.sleep(2)


    def test_two(self):
        self.driver.get('http://workntutor.com')
        print('The title of the page is', self.driver.title)
        time.sleep(2)

    def test_three(self):
        self.driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
        print('The title of the page is', self.driver.title)
        time.sleep(2)

    def test_four(self):
        self.driver.get('https://linuxjobber.com')
        print('The title of the page is', self.driver.title)
        time.sleep(2)



#  Automation Login

    def test_login(self):


        self.driver = webdriver.Chrome (executable_path='C:\Web Drivers\chromedriver.exe')
        self.driver.get('https://chatscrum.com')
        login = self.driver.find_element_by_xpath('/html/body/app-root/app-home/div[1]/nav/div/div/ul/li[1]/a/b')
        login.click()
        email_test = self.driver.find_element_by_xpath(
            '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[1]/input')
        email_test.send_keys(email)

        password_test = self.driver.find_element_by_xpath(
            '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[2]/input')
        password_test.send_keys(password)

        project_test = self.driver.find_element_by_xpath(
            '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[3]/input')
        project_test.send_keys(project)
        time.sleep(1)
        login_btn = self.driver.find_element_by_xpath(
            '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[4]/button')
        login_btn.click()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):  # Executes once after all other tests
        print('Closing Test cases')


if __name__ == '__main__':  # To make the code run call the main method from the unit test module
    unittest.main()