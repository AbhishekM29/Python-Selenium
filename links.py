import time
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import by
from selenium.webdriver.support.select import Select

# service_obj = Service("E:/python_study/pythonProject1/drivers/chromedriver.exe")
driver = webdriver.Firefox()
# driver= webdriver.Chrome("E:/python_study/Python_Selenium/chrome-win32/chrome-win32/chrome.exe")
driver.get("https://www.google.com")
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
        # print(req.status_code)
        print("broken links are", url,req.status_code)
    # else:
    #     print("valid URls", url)

driver.close()