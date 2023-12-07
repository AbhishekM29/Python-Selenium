import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:/python_study/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://demoqa.com/nestedframes")

driver.maximize_window()

driver.switch_to.frame("frame1")

txt = driver.find_element(By.XPATH, "/html/body").text
childFrame = driver.find_element(By.XPATH, "/html/body/iframe")
driver.switch_to.frame(childFrame)
childtxt = driver.find_element(By.XPATH, "/html/body").text
print((childtxt))

print(txt)
