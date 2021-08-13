from selenium import webdriver
# from selenium.webdriver.common.keys import keys
import time
# Aisha Idowu
# Task 8

# driver = webdriver.Chrome(executable_path='C:\Web Drivers\chromedriver.exe')
driver = webdriver.Firefox(executable_path='C:\Web Drivers\geckodriver.exe')

driver.get('https://chatscrum.com')
print(driver.title)

driver.get('https://www.google.com/')
time.sleep(3)
print(driver.title)

driver.get('http://demo.automationtesting.in/Register.html')
print(driver.title)


driver.back()
time.sleep(3)
print(driver.title)


driver.forward()
time.sleep(3)
print(driver.title)


driver.close()
