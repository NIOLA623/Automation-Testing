from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys

# Aisha Idowu
# Task 19

chrome_driver = webdriver.Chrome(executable_path='C:\Web Drivers\chromedriver.exe')
chrome_driver.maximize_window()

chrome_driver.get('https://linuxjobber.com')
print(chrome_driver.title)
login = chrome_driver.find_element_by_link_text('Log In').click()
email = chrome_driver.find_element_by_xpath('/html/body/section/div/div/div[1]/div/form/div[1]/input')
password = chrome_driver.find_element_by_xpath('/html/body/section/div/div/div[1]/div/form/div[2]/input')
email.send_keys('idowumofolorunsho@gmail.com')
password.send_keys('DearJobber')

login_btn = chrome_driver.find_element_by_xpath('/html/body/section/div/div/div[1]/div/form/div[5]/button').click()
learn = chrome_driver.find_element_by_xpath('/html/body/header/div/div/div/div[2]/div[1]/nav/ul/li[2]/a')
automation_testing = chrome_driver.find_element_by_xpath('/html/body/header/div/div/div/div[2]/div[1]/nav/ul/li[2]/div/div/div[5]/ul/li[1]/a')

actions = ActionChains(chrome_driver)
actions.move_to_element(learn).click().pause(2).move_to_element(automation_testing).click().perform()
time.sleep(3)
chrome_driver.close()