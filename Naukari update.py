import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
username = 'mohammadshaik776@gmail.com'
password = 'Mohammad47@'
path = os.path.abspath("C:\Resume\Mohammad_Automation_Engineer.pdf")
driver.get('https://www.naukri.com/nlogin/login')
time.sleep(15)
driver.find_element(By.ID, 'usernameField').send_keys(username)
time.sleep(5)
driver.find_element(By.ID, 'passwordField').send_keys(password)
driver.find_element(By.XPATH, '//button[text()="Login"]').click()
time.sleep(5)
driver.get('https://www.naukri.com/mnjuser/profile?id=&orgn=homepage')
time.sleep(5)
driver.find_element(By.XPATH, "//input[@type='file']").send_keys(path)
time.sleep(5)
driver.quit()
