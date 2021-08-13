from selenium import webdriver
import time
# Aisha Idowu
#  Task 7
chrome_driver = webdriver.Chrome(executable_path='C:\Web Drivers\chromedriver.exe')
chrome_driver.get('https://chatscrum.com')
print(chrome_driver.title)
print(chrome_driver.current_url)

# Sign up
signup_button = chrome_driver.find_element_by_xpath('/html/body/app-root/app-home/div[1]/nav/div/div/ul/li[2]/a/button')
signup_button.click()
# email
email_detail = chrome_driver.find_element_by_xpath('/html/body/app-root/app-signup/div[1]/div/div/div[1]/div/form/div[1]/div[1]/input')
email_detail.send_keys('idowumofolorunsho@gmail.com')
# password
password_detail = chrome_driver.find_element_by_xpath('/html/body/app-root/app-signup/div[1]/div/div/div[1]/div/form/div[1]/div[2]/input')
password_detail.send_keys('DearChat23%')
# full name
name_detail = chrome_driver.find_element_by_xpath('/html/body/app-root/app-signup/div[1]/div/div/div[1]/div/form/div[1]/div[3]/input')
name_detail.send_keys('Aisha Idowu')
# user
user = chrome_driver.find_element_by_xpath('/html/body/app-root/app-signup/div[1]/div/div/div[1]/div/form/div[1]/div[4]/div/label/div')
user.click()
# Project name
project_detail = chrome_driver.find_element_by_xpath('/html/body/app-root/app-signup/div[1]/div/div/div[1]/div/form/div[1]/div[5]/input')
project_detail.send_keys('Web-drivers commands')
# signup button
signup = chrome_driver.find_element_by_xpath('/html/body/app-root/app-signup/div[1]/div/div/div[1]/div/form/div[2]/button')
signup.click()
time.sleep(5)

# login
login = chrome_driver.find_element_by_xpath('/html/body/app-root/app-signup/div[1]/nav/div/div/ul/li[1]/a/b')
login.click()
# login email
login_email = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[1]/input')
login_email.send_keys('idowumofolorunsho@gmail.com')
# login password
login_password = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[2]/input')
login_password.send_keys('DearChat23%')
# login projectname
login_project = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[3]/input')
login_project.send_keys('Web-drivers commands')
# login button
login_btn = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[4]/button')
login_btn.click()
time.sleep(5)
chrome_driver.close()









