import time
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_object = Service("D:/python_study/drivers/chromedriver.exe")
sleep(5)
driver = webdriver.Chrome(service=service_object)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
SearchBox = driver.find_element(By.CSS_SELECTOR, "#Wikipedia1_wikipedia-search-input")
if SearchBox.is_enabled():
    print("Search Box is enabled")
    SearchBox.send_keys("Lumia")
    driver.find_element(By.XPATH,
                        "//body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[4]/div[2]/div[1]/aside["
                        "1]/div[1]/div[1]/div[1]/form[1]/div[1]/span[2]/span[2]/input[1]").click()

FirstName = driver.find_element(By.XPATH,
                                "//body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[4]/div[2]/div["
                                "1]/aside[1]/div[1]/div[1]/div[1]/form[1]/div[1]/span[2]/span[2]/input[1]")
if FirstName.is_displayed():
    print("First Name template Displayed")
driver.find_element(By.XPATH, "//button[contains(text(),'Click Me')]").click()
time.sleep(4)
driver.switch_to.alert.accept()

drop_down = driver.find_element(By.XPATH, "//select[@id='speed']")
select = Select(drop_down)

all_options = select.options
print("total options are", len(all_options))

for opt in all_options:   
    name_options = opt.text

    print("All present Options are", name_options)

select.select_by_visible_text("Faster")

select_file = driver.find_element(By.XPATH, "//select[@id='files']")
select1 = Select(select_file)

select1.select_by_value("3")

select_number = driver.find_element(By.XPATH, "//select[@id='number']")

select2 = Select(select_number)

select2.select_by_index(2)

txt_lables = driver.find_element(By.XPATH, "//span[contains(text(),'Message_12')]")
print(txt_lables.text)

txt_lables1 = driver.find_element(By.XPATH, "//span[contains(text(),'Message-123')]")
if txt_lables1.text == "Message-123":
    print("yes correct", txt_lables1.text)

david = driver.find_element(By.XPATH, "//name[contains(text(),'David')]")
if david.is_displayed():
    print(david.text)

elements = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']")
print(len(elements))

all_links = driver.find_elements(By.TAG_NAME, 'a')
print("Total links are :", len(all_links))

driver.quit()
