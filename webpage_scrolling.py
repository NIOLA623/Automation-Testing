from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Aisha Idowu
# Task 18

chrome_driver = webdriver.Chrome(executable_path='C:\Web Drivers\chromedriver.exe')
chrome_driver.maximize_window()

chrome_driver.get('https://www.wikipedia.org/')
print(chrome_driver.title)

search_box = chrome_driver.find_element_by_name('search')
search_box.send_keys('Python Programming Language')
# Scroll by Pixel
search = chrome_driver.find_element_by_xpath('/html/body/div[3]/form/fieldset/button').click()
scroll1 = chrome_driver.execute_script("window.scrollBy(0, 300)", "")  # Scroll by Pixel
time.sleep(3)

# Scroll till element is found
chrome_driver.execute_script("window.open(' ');") # Switch to a new tab
chrome_driver.switch_to.window(chrome_driver.window_handles[-1])  # Handle must be a string
chrome_driver.get('https://www.wikipedia.org/')
time.sleep(3)

search_box = chrome_driver.find_element_by_name('search')
search_box.send_keys('Python Programming Language')

search_btn = chrome_driver.find_element_by_xpath('/html/body/div[3]/form/fieldset/button').click()
description = chrome_driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]/div[1]/table[2]/tbody/tr[1]/th[3]')
chrome_driver.execute_script("arguments[0].scrollIntoView()", description)  # Scroll till element is found method
time.sleep(3)

# Scroll till the end of page
chrome_driver.execute_script("window.open(' ');")
chrome_driver.switch_to.window(chrome_driver.window_handles[-1])  # Handle must be a string
chrome_driver.get('https://www.wikipedia.org/')
time.sleep(3)

search_box = chrome_driver.find_element_by_name('search')
search_box.send_keys('Python Programming Language')

search_btn = chrome_driver.find_element_by_xpath('/html/body/div[3]/form/fieldset/button').click()
chrome_driver.execute_script('window.scrollBy(0,document.body.scrollHeight)') # Scroll till end of page method
time.sleep(3)

chrome_driver.execute_script("window.open(' ');")
chrome_driver.switch_to.window(chrome_driver.window_handles[-1])  # Handle must be a string
chrome_driver.get('https://www.wikipedia.org/')
time.sleep(3)

search_box = chrome_driver.find_element_by_name('search')
search_box.send_keys('Python Programming Language')

search_btn = chrome_driver.find_element_by_xpath('/html/body/div[3]/form/fieldset/button').click()
# Scroll till end of page
html = chrome_driver.find_element_by_tag_name("html")
time.sleep(3)

frameworks = chrome_driver.find_element_by_link_text('web frameworks').click()
time.sleep(3)

chrome_driver.quit()