import time
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("D:/python_study/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()


all_links = driver.find_elements(By.TAG_NAME, 'a')
print("Total links are :", len(all_links))

for link in all_links:
    url = link.get_attribute("href")
    try:
        req = requests.head(url)
    except:
        None

    if req.status_code >= 400:
        print("broken links are", url)
    else:
        print("valid URls", url)

driver.close()