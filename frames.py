from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException


# Aisha Idowu
# Task 16

chrome_driver = webdriver.Chrome(executable_path='C:\Web Drivers\chromedriver.exe')
chrome_driver.maximize_window()

chrome_driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')
print(chrome_driver.title)

try:
    chrome_driver.switch_to.frame('packageListFrame')
    link1 = chrome_driver.find_element_by_link_text('org.openqa.selenium.cli').click()
    time.sleep(3)

    chrome_driver.switch_to.default_content()  # Back to the default page
    chrome_driver.switch_to.frame('packageFrame')
    chrome_driver.find_element_by_link_text('AjaxElementLocator').click()
    time.sleep(2)
    chrome_driver.switch_to.default_content()

except NoSuchElementException as exe:
    print(exe)


time.sleep(3)
chrome_driver.close()
