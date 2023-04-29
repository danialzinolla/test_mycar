import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *


se = Service(executable_path='/Users/danial/Downloads/chromedriver_mac_arm64/chromedriver')
driver = webdriver.Chrome(service=se)

try:
    driver.maximize_window()
    driver.get('https://sandbox.mycarpro.net/')
    time.sleep(3)
    email_login = driver.find_element(By.ID, 'login__email')
    email_login.clear()
    email_login.send_keys('l.pan@mycar.kz')
    password_login = driver.find_element(By.ID, 'login__password')
    password_login.clear()
    password_login.send_keys('mycar123')
    password_login.send_keys(Keys.ENTER)
    time.sleep(5)
    raise WebDriverException("Incorrect password")

# except NoSuchElementException as email_login:
#     print("Не удалось сорри", email_login)
except NoSuchElementException:
    print("Element not found")
except WebDriverException as password_login:
    print("Error occurred:", password_login)
    # except NoSuchElementException as password_login:
    #     password_login = "Incorrect password"
    #     raise password_login

# except Exception as email_login:
#     print("Произошла ошибка", email_login)

finally:
    driver.close()
    driver.quit()

