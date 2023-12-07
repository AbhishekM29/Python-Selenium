import time
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("D:/python_study/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://testautomationpractice.blogspot.com/")

# rows = driver.find_elements(By.XPATH, "//body/div[4]/div[2]/div[2]/div[2]/footer[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody/tr")
# numrows = len(rows)
# print(numrows)
# coloumns = driver.find_elements(By.XPATH, "//tbody/tr/th")
# numcoloums = len(coloumns)
# print(numcoloums)
# for r in range(2,numrows):
#     for c in range(1,numcoloums):
#      r1c1=driver.find_element(By.XPATH, "//tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#      print(r1c1,end='')
#      print()
driver.switch_to.frame("frame-one1434677811")
driver.find_element(By.XPATH, "/html/head/link[3]").click()