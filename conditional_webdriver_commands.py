from selenium import webdriver
import time
# Aisha Idowu
# Task 9
chrome_driver = webdriver.Chrome(executable_path= 'C:\Web Drivers\chromedriver.exe')
chrome_driver.get('https://chatscrum.com')
print(chrome_driver.title)
login = chrome_driver.find_element_by_xpath('/html/body/app-root/app-home/div[1]/nav/div/div/ul/li[1]/a/b')
print('The display status is', login.is_displayed())
print('The enable status is', login.is_enabled())
login.click()
# email
email = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[1]/input')
print('The display status is', email.is_displayed())
print('The enable status is', email.is_enabled())
# password
password = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[2]/input')
print('The display status is', password.is_displayed())
print('the enable status is', password.is_enabled())
# Project name
project = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[3]/input')
print('The display status is', project.is_displayed())
print('The enable status is', project.is_enabled())
# Conditional statement
if email.is_enabled() and email.is_displayed() and password.is_displayed() and password.is_enabled() and project.is_enabled() and project.is_displayed():
    email.send_keys('idowumofolorunsho@gmail.com')
    password.send_keys('DearChat23%')
    project.send_keys('Web-drivers commands')
    time.sleep(5)
    login_button = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[4]/button')
    login_button.click()


# automation section
chrome_driver.get('http://demo.automationtesting.in/Register.html')
print(chrome_driver.title)
first_name = chrome_driver.find_element_by_xpath('/html/body/section/div/div/div[2]/form/div[1]/div[1]/input')
print('The display status is', first_name.is_displayed())
print('The enabled status is', first_name.is_enabled())

hobbies = chrome_driver.find_element_by_xpath('/html/body/section/div/div/div[2]/form/div[6]/div/div[1]/input')
print('The selected status is', hobbies.is_selected())
hobbies.click()
print('The selected status is', hobbies.is_selected())
time.sleep(5)


chrome_driver.close()


