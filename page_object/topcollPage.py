'''
@filename: /topcollPage
@time: 2023/10/7 16:03
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_object.basePage import BasePage
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

SNAPSHOTS_DIR = 'snapshots'


class TopcollPage(BasePage):
	file_path = './data/top_coll/data.yaml'

	# 页面url
	url = 'https://nftgo.io/discover/top-collections'

	# 页面元素
	# tanchuang = (By.XPATH, '//span[@class="sc-bczRLJ sc-gsnTZi fNQVyA fuKjun pop-up-modal_closeIcon__Jst7n"]')
	# search_click = (By.XPATH, '//input[@class="search-input_searchInput__hmtqI"]')

	def open_topcoll(self):
		self.driver.get(self.url)
		# self.click(self.tanchuang)
		self.parse_action(self.file_path, 'open_topcoll')

	def search_coll(self):
		# self.send_keys(self.search_click, keyword)

		self.parse_action(self.file_path, 'search_coll')

		self.wait(3)

	def hover_marketCap(self):
		self.parse_action(self.file_path,'hover_marketCap')