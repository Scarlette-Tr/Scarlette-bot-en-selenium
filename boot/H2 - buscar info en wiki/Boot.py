from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time,json

#Histria 2 una persona esta realizando una clase de programacion y busca informacion en wikipedia y le tira una foto#

driver= webdriver.Firefox(executable_path="driver/geckodriver.exe")

with open("bus.json") as json_file:
    data = json.load(json_file)
    for p in data["buscar"]:
        driver.get("https://www.wikipedia.org/")
        bara = driver.find_element(By.NAME,"search")
        bara.send_keys(p["bus"])
        bara.send_keys(Keys.ENTER)
        time.sleep(3)
        driver.get_screenshot_as_file("img/"+p["bus"]+".png")
        time.sleep(3)

driver.close()

