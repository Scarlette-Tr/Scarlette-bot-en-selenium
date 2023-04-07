from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time,json

#usuario busca video de como hacer las un boot usando selenium para una clase#



driver= webdriver.Firefox(executable_path="driver/geckodriver.exe")

driver.get("https://www.youtube.com/")
bara = driver.find_element(By.NAME,"search_query")
bara.send_keys("como hacer un Boot usando selenium")
time.sleep(3)
bara = driver.find_element(By.ID,"search-icon-legacy")
bara.send_keys(Keys.ENTER)
time.sleep(10)
driver.close()

