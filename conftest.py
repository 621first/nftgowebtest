'''
@filename: /conftest.py
@time: 2023/9/20 14:15
'''

import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
sys.dont_write_bytecode = True

# 注册插件
pytest_plugins = ["commons.plugin"]


@pytest.fixture(scope="session",autouse=True)
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()


    # driver.get('https://nftgo.io')
    # driver.find_element(By.XPATH,'//span[@class="sc-bczRLJ sc-gsnTZi fNQVyA fuKjun pop-up-modal_closeIcon__Jst7n"]').click()



    yield driver
    driver.quit()