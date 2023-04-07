from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json,time

#Historia 1: una persona estaba buscando piezas para su PC#

driver= webdriver.Firefox(executable_path="driver/geckodriver.exe")

with open("txt.json") as json_file:
    data=json.load(json_file)

    for p in data["busqueda"]:
        driver.get("https://es.aliexpress.com/?gatewayAdapt=glo2esp")
        time.sleep(2)
        bus = driver.find_element(By.NAME,"SearchText")
        bus.send_keys(p["bus"])
        time.sleep(2)
        btn=driver.find_element(By.CLASS_NAME,"search-button")
        btn.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.get_screenshot_as_file("img/"+p["bus"]+".png")
        time.sleep(5)
driver.close()
driver.quit()