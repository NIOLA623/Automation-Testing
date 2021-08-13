from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By

# AISHA IDOWU
# TASK 13
chrome_driver = webdriver.Chrome(executable_path='C:\Web Drivers\chromedriver.exe')
chrome_driver.maximize_window()

chrome_driver.get('https://chatscrum.com')
print(chrome_driver.title)

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
login_project.send_keys('Web-drivers commands')
time.sleep(2)
# login button
login_btn = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[4]/button')
login_btn.click()
time.sleep(3)
# Pop-up close
pop_close = chrome_driver.find_element_by_class_name('slackclose')
pop_close.click()
time.sleep(5)
# Explicitly wait
wait = WebDriverWait(chrome_driver, 100)
wait.until(EC.presence_of_element_located((By.ID, 'home-tab')))
# Task
my_task = chrome_driver.find_element_by_id('home-tab')
my_task.click()
# Add Note
add_note = chrome_driver.find_element(By.ID, 'addNoteBtn')
add_note.click()
# High
high = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[4]/div/div[1]/div[2]/form/div[2]/input[1]')
high.click()
print('The selected status of high is', high.is_selected())
# Medium
medium = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[4]/div/div[1]/div[2]/form/div[2]/input[2]')
medium.click()
print('The selected status of medium is', medium.is_selected())
# Low
low = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[4]/div/div[1]/div[2]/form/div[2]/input[3]')
low.click()
print('The selected status of low is', low.is_selected())
time.sleep(5)
chrome_driver.close()
