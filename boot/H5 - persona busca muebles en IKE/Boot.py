from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time,json

#usuario busca Alfombras para su casa en IKEA#



driver= webdriver.Firefox(executable_path="driver/geckodriver.exe")

driver.get("https://www.ikea.com.do/es")
bara = driver.find_element(By.ID,"header_searcher_desktop_input")
bara.send_keys("Alfombras")
bara.send_keys(Keys.ENTER)
time.sleep(10)
driver.close()

