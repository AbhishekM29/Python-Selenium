import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:/python_study/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Prompt')]").click()
time.sleep(5)
alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.send_keys("Abhishek Vijay Mujumdar")
time.sleep(5)
alert_window.accept()
time.sleep(5)