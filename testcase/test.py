'''
@filename: /test
@time: 2023/9/19 16:45
'''
from selenium import webdriver
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://selenium.dev")
time.sleep(1)
driver.quit()