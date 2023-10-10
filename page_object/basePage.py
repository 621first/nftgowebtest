'''
@filename: /basePage
@time: 2023/10/7 15:38
'''

import os
import time

import allure
import yaml
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from commons.utils.log import get_logger
SNAPSHOTS_DIR = "snapshots"

class BasePage:

	logger = get_logger()

	def __init__(self, driver):
		self.driver = driver

	def visit(self):
		self.driver.get(self.url)

	# 元素定位
	def locator(self, ele):
		style = 'background: green; border: 2px solid red;'
		js = 'arguments[0].setAttribute("style", arguments[1]);'
		try:
			WebDriverWait(self.driver, 3).until(
				EC.presence_of_element_located(ele)
			)
		except Exception as e:

			# 截图保存到本地
			# os.makedirs(SNAPSHOTS_DIR, exist_ok=True)  # 创建目录（如果不存在）
			# self.driver.save_screenshot(os.path.join(SNAPSHOTS_DIR, snapshot_file))

			# 截图保存到allure
			screenshot  = self.driver.get_screenshot_as_png()
			allure.attach(screenshot,attachment_type=allure.attachment_type.PNG)

			raise e
		else:
			screenshot  = self.driver.get_screenshot_as_png()
			allure.attach(screenshot,attachment_type=allure.attachment_type.PNG)

			element = self.driver.find_element(*ele)
			self.driver.execute_script(js, element, style)
		return element



		# return self.driver.find_element(*ele)

	# 输入文本
	def send_keys(self, ele, val):
		self.locator(ele).send_keys(val)

	# 清除文本
	def clear(self,ele):
		self.locator(ele).clear()

	# 获取元素文本
	def text(self,ele):
		self.locator(ele).text

	# 单击
	def click(self, ele):
		self.locator(ele).click()

	def js_click(self,ele):
		self.driver.execute_script('arguments[0].click();',ele)

	# 获取元素属性
	def get_value(self, loc):
		# element.get_attribute("attribute_name")
		return self.locator(loc).get_attribute('value')

	def hover(self,ele):
		ActionChains(self.driver).move_to_element(self.locator(ele)).perform()
		self.wait(3)

	# 滚动页面
	def execute_script(self,ele):
		self.driver.execute_script('arguments[0].scrollIntoView();',self.locator(ele))

	# 双击元素
	def double_click(self,ele):
		action = ActionChains(driver)
		action.double_click(self.locator(ele)).perform()

	# 拖拽元素
	def drag_and_drop(self,source_element,target_element):
		action = ActionChains(driver)
		action.drag_and_drop(self.locator(source_element), self.locator(target_element)).perform()





	# 等待
	def wait(self, time_):
		time.sleep(time_)





	# def find_element(self,driver, by, value, timeout=5):
	# 	style = 'background: green; border: 2px solid red;'
	# 	js = 'arguments[0].setAttribute("style", arguments[1]);'
	# 	try:
	# 		WebDriverWait(self.driver, timeout).until(
	# 			EC.presence_of_element_located((by, value))
	# 		)
	# 	except Exception as e:
	# 		snapshot_file = 'snapshot_%s.png' % int(time.time())
	# 		os.makedirs(SNAPSHOTS_DIR, exist_ok=True)  # 创建目录（如果不存在）
	# 		self.driver.save_screenshot(os.path.join(SNAPSHOTS_DIR, snapshot_file))
	# 		raise NoSuchElementException('%s 秒内未找到元素 %s=%s' % (timeout, by, value))
	# 	else:
	# 		element = self.driver.find_element(by, value)
	# 		self.driver.execute_script(js, element, style)
	# 	return element
	#
	#
	#
	# def find_elements(self,driver, by, value, timeout=5):
	# 	style = 'background: green; border: 2px solid red;'
	# 	js = 'arguments[0].setAttribute("style", arguments[1]);'
	# 	try:
	# 		WebDriverWait(self.driver, timeout).until(
	# 			EC.presence_of_element_located((by, value))
	# 		)
	# 	except TimeoutException:
	# 		snapshot_file = 'snapshot_%s.png' % int(time.time())
	# 		os.makedirs(SNAPSHOTS_DIR, exist_ok=True)  # 创建目录（如果不存在）
	# 		self.driver.save_screenshot(os.path.join(SNAPSHOTS_DIR, snapshot_file))
	# 		raise NoSuchElementException('%s 秒内未找到元素 %s=%s' % (timeout, by, value))
	# 	else:
	# 		element = driver.find_elements(by, value)
	# 		# self.driver.execute_script(js, element, style)
	# 	return element


	def parse_action(self, path, fun_name):
		params = {}
		with open(path, 'r', encoding='utf-8') as f:
			funtion = yaml.safe_load(f)
			steps: List[Dict] = funtion[fun_name]

			for step in steps:
				if step['action'] == "send_keys":
					self.send_keys([step['by'], step['locator']],step['keyword'])
				if step['action'] == "click":
					self.click([step['by'], step['locator']])
				if step['action'] == 'hover':
					self.hover([step['by'], step['locator']])
