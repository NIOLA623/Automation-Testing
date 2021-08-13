from selenium import webdriver
import time
# Aisha Idowu
# Task 10
chrome_driver = webdriver.Chrome(executable_path= 'C:\Web Drivers\chromedriver.exe')
chrome_driver.get('https://chatscrum.com')
# Implicit wait of 10s
chrome_driver.implicitly_wait(10)
# Title assertion
assert "Scrum" in chrome_driver.title

# Login
login = chrome_driver.find_element_by_xpath('/html/body/app-root/app-home/div[1]/nav/div/div/ul/li[1]/a/b')
login.click()
time.sleep(2)
# login email
login_email = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[1]/input')
login_email.send_keys('idowumofolorunsho@gmail.com')
# login password
login_password = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[2]/input')
login_password.send_keys('DearChat23%')
# login projectname
login_project = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[3]/input')
login_project.send_keys('Test Jobber')
# login button
login_btn = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[4]/button')
login_btn.click()
time.sleep(3)

chrome_driver.close()

