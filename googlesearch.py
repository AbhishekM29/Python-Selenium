import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# service_object = Service("D:/python_study/drivers/chromedriver.exe")
# sleep(5)
# driver = webdriver.Chrome(service=service_object)
driver=webdriver.Firefox()
driver.get("https://google.com/")
driver.maximize_window()
driver.implicitly_wait(5)

mywait = WebDriverWait(driver, 10, ignored_exceptions=Exception)


searchbox = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
searchbox.send_keys("flipkart")
searchbox.submit()

selenium1 = mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']"))).click()

#selenium1 = driver.find_element(By.XPATH, "//h3[text()='Selenium']")