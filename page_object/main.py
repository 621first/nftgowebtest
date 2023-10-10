'''
@filename: /main
@time: 2023/10/10 13:52
'''
from selenium.webdriver.common.by import By
from page_object.basePage import BasePage


from selenium import webdriver

class MainPage(BasePage):
	file_path = './data/main/data.yaml'

	# 页面url
	url = 'https://nftgo.io'

	def login(self):
		self.driver.get(self.url)
		self.parse_action(self.file_path, 'open_topcoll')

		self.wait(3)

		self.parse_action(self.file_path,'login')

		self.wait(3)