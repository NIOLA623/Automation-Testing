from selenium import webdriver
from selenium.webdriver import ActionChains
import time

# Aisha Idowu
# Task 21

chrome_driver = webdriver.Chrome(executable_path='C:\Web Drivers\chromedriver.exe')
chrome_driver.maximize_window()
chrome_driver.get('https://chatscrum.com')
print(chrome_driver.title)

# Login
login = chrome_driver.find_element_by_xpath('/html/body/app-root/app-home/div[1]/nav/div/div/ul/li[1]/a/b')
login.click()
time.sleep(2)
# login email
login_email = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[1]/input')
login_email.send_keys('idowumofolorunsho@gmail.com')
# login password
login_password = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[2]/input')
login_password.send_keys('DearChat23%')
# login projectname
login_project = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[3]/input')
login_project.send_keys('Web-drivers commands')
time.sleep(2)
# login button
login_btn = chrome_driver.find_element_by_xpath('/html/body/app-root/app-login/div[1]/div/div/div[1]/div/form/div/div[4]/button')
login_btn.click()
time.sleep(3)
# nav
nav = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[1]/div/nav/div/ul').click()
# Task
my_task = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[1]/div/nav/div/ul/li[1]/a')
my_task.click()
# Add task
add_task = chrome_driver.find_element_by_id('addTaskBtn')
add_task.click()
time.sleep(3)
# Task 1
new_task1 = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/form/textarea')
new_task1.send_keys('New task 1')
task_btn = chrome_driver.find_element_by_id('submitaddTaskBtn').click()
time.sleep(3)
# Task 2
new_task2 = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/form/textarea')
new_task2.send_keys('New task 2')
task_btn = chrome_driver.find_element_by_id('submitaddTaskBtn').click()
time.sleep(3)
# Task 3
new_task3 = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/form/textarea')
new_task3.send_keys('New task 3')
task_btn = chrome_driver.find_element_by_id('submitaddTaskBtn').click()
time.sleep(3)
# Task 4
new_task4 = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/form/textarea')
new_task4.send_keys('New task 4')
task_btn = chrome_driver.find_element_by_id('submitaddTaskBtn').click()
time.sleep(3)
# Drag and Drop Actions
first_move = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[15]/div/div/div[1]/details/div/div/div[1]/div/div/div[4]/div/div/div[3]')
target1 = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[15]/div/div/div[1]/details/div/div/div[2]/div/div')
actions = ActionChains(chrome_driver)
actions.drag_and_drop(first_move, target1).perform()
time.sleep(1)

second_move = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[15]/div/div/div[1]/details/div/div/div[1]/div/div/div[3]/div/div')
target1 = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[15]/div/div/div[1]/details/div/div/div[2]/div/div')
actions = ActionChains(chrome_driver)
actions.drag_and_drop(second_move, target1).perform()
time.sleep(1)


third_move = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[15]/div/div/div[1]/details/div/div/div[1]/div/div/div[2]/div/div')
target1 = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[15]/div/div/div[1]/details/div/div/div[2]/div/div')
actions = ActionChains(chrome_driver)
actions.drag_and_drop(third_move, target1).perform()
time.sleep(1)

move = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[15]/div/div/div[1]/details/div/div/div[1]/div/div/div[4]/div/div/div[3]')
target = chrome_driver.find_element_by_xpath('/html/body/app-root/app-scrumboard/div[2]/div[2]/div/div/div[1]/div/div[15]/div/div/div[1]/details/div/div/div[2]/div/div')
actions = ActionChains(chrome_driver)
actions.drag_and_drop(move, target).perform()
time.sleep(3)

chrome_driver.close()
