import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_nuakri_update():
    driver = webdriver.Chrome()
    path = os.path.abspath("C:\Users\Ankita Sharma\Downloads\Ankita cv.pdf")
    driver.get('https://www.naukri.com/nlogin/login')
    time.sleep(2)
    driver.find_element(By.ID, 'usernameField').send_keys('60ankitasharma@gmail.com')
    driver.find_element(By.ID, 'passwordField').send_keys("Ankita@123")
    driver.find_element(By.XPATH, '//button[text()="Login"]').click()
    time.sleep(2)
    driver.get('https://www.naukri.com/mnjuser/profile?id=&orgn=homepage')
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(path)
    time.sleep(5)
    driver.quit()
