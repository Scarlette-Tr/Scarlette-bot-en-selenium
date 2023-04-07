from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time,json

#estidiante se quiere logiarse en la plataforma del itla#

usuario="202010232"
pas="Scarlette#1418"

driver= webdriver.Firefox(executable_path="driver/geckodriver.exe")

driver.get("https://plataformavirtual.itla.edu.do/login/index.php")
bara = driver.find_element(By.NAME,"username")
bara.send_keys(usuario)
time.sleep(3)
bara = driver.find_element(By.NAME,"password")
bara.send_keys(pas)
time.sleep(3)
bara = driver.find_element(By.ID,"loginbtn")
bara.send_keys(Keys.ENTER)
time.sleep(10)
driver.close()

