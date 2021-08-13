from selenium import webdriver
from selenium.webdriver import ActionChains
import time


# Aisha Idowu
# Task 20

chrome_driver = webdriver.Chrome(executable_path='C:\Web Drivers\chromedriver.exe')
chrome_driver.maximize_window()

chrome_driver.get('http://demo.guru99.com/test/simple_context_menu.html')
print(chrome_driver.title)

double_click = chrome_driver.find_element_by_xpath('/html/body/button')
actions = ActionChains(chrome_driver)
actions.double_click(double_click).perform()
time.sleep(30)

alert = chrome_driver.switch_to.alert  # switch to the alert box
alert.accept()  # click on the okay of alert box
time.sleep(3)

right_click = chrome_driver.find_element_by_xpath('/html/body/span')
actions = ActionChains(chrome_driver)
actions.context_click(right_click).perform()
time.sleep(5)
chrome_driver.close()