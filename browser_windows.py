from selenium import webdriver
import time

# Aisha Idowu
# Task 17

chrome_driver = webdriver.Chrome(executable_path='C:\Web Drivers\chromedriver.exe')
chrome_driver.maximize_window()

chrome_driver.get('https://chatscrum.com')
print(chrome_driver.title)


# print(chrome_driver.current_window_handle)  #O/P the current window handle
# chrome_driver.window_handles - returns multiple window handles

chrome_driver.execute_script("window.open(' ');")
chrome_driver.switch_to.window(chrome_driver.window_handles[-1])  # Handle must be a string
chrome_driver.get('https://linuxjobber.com')
time.sleep(3)

chrome_driver.execute_script("window.open(' ');")
chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
chrome_driver.get('https://google.com')
print(chrome_driver.title)
time.sleep(3)



chrome_driver.execute_script("window.open(' ');")
chrome_driver.switch_to.window(chrome_driver.window_handles[0])
chrome_driver.get('https://bing.com')
time.sleep(3)
if chrome_driver.title == 'Bing':
    chrome_driver.close()

chrome_driver.switch_to.window(chrome_driver.window_handles[0])
print(chrome_driver.title)
time.sleep(5)
chrome_driver.close()
