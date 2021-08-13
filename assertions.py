from selenium import webdriver
import time
import unittest

# Aisha Idowu
# Task 25



class Test(unittest.TestCase):
    def test_one(self):
        self.driver = webdriver.Chrome(executable_path='C:\Web Drivers\chromedriver.exe')

        self.driver.get('https://chatscrum.com')
        self.driver.maximize_window()
        title = self.driver.title
        self.assertEqual('Scrum', title, 'Webpage name are the same')
        self.assertNotEqual('Login', title, 'Webpage name is not Login')   # Pass because webpage name is not the same
        self.assertIn('Srumboard', title)   # Fails because Scrumboard is not in title
        self.assertFalse(title == 'Scrum') # Test fails because title is the same which is true

        login = self.driver.find_element_by_xpath('/html/body/app-root/app-home/div[1]/nav/div/div/ul/li[1]/a/b')
        login.click()
        time.sleep(2)
        # login email
        login_email = self.driver.find_element_by_xpath(
            '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[1]/input')
        login_email.send_keys('idowumofolorunsho@gmail.com')
        # login password
        login_password = self.driver.find_element_by_xpath(
            '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[2]/input')
        login_password.send_keys('DearChat23%')
        # login projectname
        login_project = self.driver.find_element_by_xpath(
            '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[3]/input')
        login_project.send_keys('Web-drivers commands')
        time.sleep(2)
        # login button
        login_btn = self.driver.find_element_by_xpath(
            '/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[4]/button')
        login_btn.click()
        time.sleep(3)

        taskTitle = 'My Tasks'
        self.assertTrue(taskTitle == 'My Tasks')

        self.driver.close()

if __name__ == '__main__':  # To make the code run call the main method from the unit test module
    unittest.main()





