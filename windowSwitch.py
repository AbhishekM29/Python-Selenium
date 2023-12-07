import time
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

servie_obj = Service("D:/python_study/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=servie_obj)

driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()

newTab = driver.find_element(By.ID, "tabButton")
newTab.click()
time.sleep(3)
current_title = driver.title
print("current title", current_title)
winIds = driver.window_handles
print(winIds)
parentwindow = winIds[0]
childwindow = winIds[1]
time.sleep(3)
driver.switch_to.window(childwindow)
newttl = driver.find_element(By.XPATH, "//*[@id='sampleHeading']").text
print(newttl)
