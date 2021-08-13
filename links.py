from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

# Aisha Idowu
# Task 15

chrome_driver = webdriver.Chrome(executable_path='C:\Web Drivers\chromedriver.exe')
chrome_driver.maximize_window()

chrome_driver.get('https://chatscrum.com')
print(chrome_driver.title)

links = chrome_driver.find_elements(By.TAG_NAME, 'a')  # locate all the link on the page
print('There are', len(links), 'links on the webpage')  # O/p all the links
for link in links:
    print(link.get_attribute('href'))

# To click on a specific link
# chrome_driver.find_element(By.LINK_TEXT, 'LOGIN').click()
# chrome_driver.find_element(By.PARTIAL_LINK_TEXT, 'LOG').click()

for link in links:
    link = link.get_attribute('href')
    # To check if a link is none valued
    if link is None:
        continue
    status = requests.head(link)  # Head method of the request module & link variable use in loop
    if status.status_code != 404:   # Comparing our link to 404 status
        print('The link is not broken')
    else:
        print('This link  is broken')

time.sleep(4)
chrome_driver.close()

