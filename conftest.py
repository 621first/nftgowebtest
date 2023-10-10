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
# pytest_plugins = ["commons.plugin"]


@pytest.fixture(scope="session",autouse=True)
def driver():
    global driver
    '''定义全局driver参数'''
    # if driver is None:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # driver.get('https://nftgo.io')
    # driver.find_element(By.XPATH,'//span[@class="sc-bczRLJ sc-gsnTZi fNQVyA fuKjun pop-up-modal_closeIcon__Jst7n"]').click()

    print("正在启动浏览器:Chrome")
    yield driver
    driver.quit()
    print("正在关闭浏览器:Chrome")



# @pytest.fixture(scope='session', autouse=True)
# def login(init_driver):
#     """
#     初始化登录，作用于全局
#     :param init_driver:
#     :return: None
#     """
#     from pages.main import Main
#     main = Main(init_driver)
#     main.login()


@pytest.fixture(scope='function')
def swhich_latest_win(init_driver):
    """测试方法后置条件：切换到当前最新窗口"""
    yield
    handles = init_driver.window_handles
    init_driver.switch_to.window(handles[-1])


@pytest.fixture(scope='function')
def close_active_win(init_driver):
    """测试方法后置条件：关闭当前活动窗口"""
    yield
    init_driver.close()


@pytest.fixture(scope='function')
def swhich_close_swhich_win(init_driver):
    """测试方法后置条件：切换到最新窗口，关闭当前活动窗口，再切换到最新窗口"""
    yield
    handles1 = init_driver.window_handles
    init_driver.switch_to.window(handles1[-1])
    init_driver.close()
    handles2 = init_driver.window_handles
    init_driver.switch_to.window(handles2[-1])


@pytest.fixture(scope='function')
def close_swhich_win(init_driver):
    """测试方法后置条件：关闭当前活动窗口，再切换到当前最新窗口"""
    yield
    init_driver.close()
    handles = init_driver.window_handles
    init_driver.switch_to.window(handles[-1])


@pytest.fixture(scope='function')
def close_swhich_close_swhich_win(init_driver):
    """测试方法后置条件：关闭当前活动窗口，再切换到当前最新窗口,再关闭当前活动窗口，再切换到当前最新窗口"""
    yield
    init_driver.close()
    handles1 = init_driver.window_handles
    init_driver.switch_to.window(handles1[-1])
    init_driver.close()
    handles2 = init_driver.window_handles
    init_driver.switch_to.window(handles2[-1])


@pytest.fixture(scope='function')
def swhich_close_swhich_close_win(init_driver):
    """测试方法后置条件：切换到最新窗口，关闭当前活动窗口，再切换到最新窗口"""
    yield
    handles1 = init_driver.window_handles
    init_driver.switch_to.window(handles1[-1])
    init_driver.close()
    handles2 = init_driver.window_handles
    init_driver.switch_to.window(handles2[-1])
    init_driver.close()