'''
@filename: /basePage
@time: 2023/10/7 15:38
'''

import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:

	def __init__(self, driver):
		self.driver = driver

	# def click(self):
	# 	pass
	#
	# def clear(self):
	# 	self._dispatch("change_value_of", (self._webelement, self._driver), "clear", ())
	#
	# def send_keys(self, *value):
	# 	self._dispatch("change_value_of", (self._webelement, self._driver), "send_keys", value)


	def find_element(self,driver, by, value, timeout=5):
		style = 'background: green; border: 2px solid red;'
		js = 'arguments[0].setAttribute("style", arguments[1]);'
		try:
			WebDriverWait(self.driver, timeout).until(
				EC.presence_of_element_located((by, value))
			)
		except TimeoutException:
			snapshot_file = 'snapshot_%s.png' % int(time.time())
			os.makedirs(SNAPSHOTS_DIR, exist_ok=True)  # 创建目录（如果不存在）
			self.driver.save_screenshot(os.path.join(SNAPSHOTS_DIR, snapshot_file))
			raise NoSuchElementException('%s 秒内未找到元素 %s=%s' % (timeout, by, value))
		else:
			element = self.driver.find_element(by, value)
			self.driver.execute_script(js, element, style)
		return element



	def find_elements(self,driver, by, value, timeout=5):
		style = 'background: green; border: 2px solid red;'
		js = 'arguments[0].setAttribute("style", arguments[1]);'
		try:
			WebDriverWait(self.driver, timeout).until(
				EC.presence_of_element_located((by, value))
			)
		except TimeoutException:
			snapshot_file = 'snapshot_%s.png' % int(time.time())
			os.makedirs(SNAPSHOTS_DIR, exist_ok=True)  # 创建目录（如果不存在）
			self.driver.save_screenshot(os.path.join(SNAPSHOTS_DIR, snapshot_file))
			raise NoSuchElementException('%s 秒内未找到元素 %s=%s' % (timeout, by, value))
		else:
			element = driver.find_elements(by, value)
			# self.driver.execute_script(js, element, style)
		return element