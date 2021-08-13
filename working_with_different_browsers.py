from selenium import webdriver
# Aisha Idowu
# Task 6

# Chrome driver test
chrome_driver = webdriver.Chrome(executable_path= 'C:\Web Drivers\chromedriver.exe')
chrome_driver.get('https://chatscrum.com')
print(chrome_driver.title)
chrome_driver.close()

# Fire fox driver test
firefox_driver = webdriver.Firefox(executable_path='C:\Web Drivers\geckodriver.exe')
firefox_driver.get('https://chatscrum.com')
print(firefox_driver.title)
firefox_driver.close()

# Microsoft Edge driver test
edge_driver = webdriver.Edge(executable_path='C:\Web Drivers\msedgedriver.exe')
edge_driver.get('https://chatscrum.com')
print(edge_driver.title)
edge_driver.close()

