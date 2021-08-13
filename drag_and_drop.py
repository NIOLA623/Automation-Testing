from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
chrome_driver = webdriver.Chrome(executable_path='C:\Web Drivers\chromedriver.exe')
chrome_driver.maximize_window()
chrome_driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
print(chrome_driver.title)

# Dropdown Selection
element = chrome_driver.find_element_by_id('RESULT_RadioButton-9')
dropdown = Select(element)

# Options selection
dropdown.select_by_visible_text('Morning')
dropdown.select_by_index('2')
dropdown.select_by_value('Radio-2')
print(len(dropdown.options))

# For loop to print options
options = dropdown.options
for option in options:
    print(option.text)

time.sleep(5)

chrome_driver.close()