from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("D:/python_study/drivers/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.get("https://google.com")
driver.maximize_window()
search_bing= driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
search_bing.click()
search_bing.send_keys("dropdown for selenium practice")
action= ActionChains(driver)
action.send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH,"//h3[contains(text(),'Practice handling dropdowns in selenium webdriver')]").click()
drp1=driver.find_element(By.XPATH,"//select[@id='first']")
select=Select(drp1)
all_opt=select.options
print("total options are",len(all_opt))
select.select_by_visible_text("Google")