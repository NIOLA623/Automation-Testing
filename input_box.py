from selenium import webdriver
from selenium.webdriver.common.by import By

# The lines of code are not complete, its just showing how to find the common attributes and number of element
# (input boxes by using the common attributes), provide values to input boxes, Methods of locating element
chrome_driver = webdriver.Chrome(executable_path='C:\Web Drivers\chromedriver.exe')
chrome_driver.maximize_window()

chrome_driver.get('https://fs29.formsite.com/bld/FormSite?FormId=LoadCreateNewForm')
print(chrome_driver.get)
inputboxes = chrome_driver.find_element(By.CLASS_NAME, 'text_field').send_keys('Aisha')
print(len(inputboxes))
chrome_driver.find_element(By.ID, 'phone').send_keys('08089908890')